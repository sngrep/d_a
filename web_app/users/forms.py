from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(
        label='Логин',
        help_text='''Принимаются латинские буквы разного регистра,
                    цифры, а так же некоторые спецсимволы (@.+-_)'''
        )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text='''<ul>
            <li>Пароль не должен быть похож на остальные регистрационные данные</li>
            <li>Пароль должен содержать не менее 8 символов</li>
            <li>Не допускаются слишком простые пароли</li>
            <li>Не допускаются пароли, состоящие из одних цифра</li>
            <li>Пароли не хранятся в чистом виде, хранятся только хэши паролей</li>
            </ul>'''
            )
    password2 = forms.CharField(label='Подтверждение пароля',
        widget=forms.PasswordInput,
        help_text='Введите повторно такой же пароль, как и в поле выше, для верификации.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
