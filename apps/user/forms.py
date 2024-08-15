from django.contrib.auth import password_validation
from django.forms import CharField, PasswordInput
from django.forms import *
from django.contrib.auth.hashers import make_password

from apps.user.models import User


class LoginForm(Form):
    username = CharField(max_length=55)
    password = CharField(widget=PasswordInput())


class RegisterForm(ModelForm):
    password = CharField(widget=PasswordInput())
    confirm_password = CharField(widget=PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)
        return password

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'password',
            'confirm_password'
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            msg = 'This username already registered'
            self.add_error('username', msg)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            msg = 'This email already registered'
            self.add_error('email', msg)
        return email

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            msg = 'Passwords do not match'
            self.add_error('confirm_password', msg)
        return self.cleaned_data

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user = User.objects.get(
            username=self.cleaned_data['username'],
        )
        user.set_password(self.cleaned_data['password'])

        user.save()
        return user
