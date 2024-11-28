from django.contrib.auth.forms import UserCreationForm
from main.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    # class UserRegisterForm(UserCreationForm):
    """Класс форма для регистрации пользователей"""
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'nick_name', 'birth_date',
                  'email', 'password1', 'password2')
