from django.contrib.auth.views import LoginView
from users.views import logout, UserCreateView, email_verification
# , UserListView, ManagerUserUpdateView
from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    # Урлы для входа пользователя в систему, выхода из системы и регистрации
    path('login/', LoginView.as_view(template_name="login.html"),
         name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', logout, name='logout'),

    # Урл для подтверждения почты
    path('email-confirm/<str:token>/', email_verification,
         name='email-confirm'),
]
