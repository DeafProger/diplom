from django.shortcuts import get_object_or_404, redirect
from config.settings import EMAIL_HOST_USER, LOGOUT_REDIRECT_URL
from django.contrib.auth.views import auth_logout
from django.views.generic import CreateView
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from users.models import User
import secrets


class UserCreateView(CreateView):
    """Класс контроллер для регистрации пользователей"""
    success_url = '/login'
    template_name = 'user_form.html'
    form_class = UserRegisterForm
    model = User

    def form_valid(self, form):
        """Метод для того, чтобы поставить пользователю статус неактивный,
        сгенерировать ему токен и отправить на почту"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/email-confirm/{token}/'
        send_mail(
            subject='Подтвердите свою электронную почту',
            message=f'Для подтверждения перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """Метод для подтверждения почты пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect('/login')


# Create your views here.
def logout(request):
    try:
        auth_logout(request)
    finally:
        return redirect(LOGOUT_REDIRECT_URL)
