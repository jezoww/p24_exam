from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.forms import PasswordInput


# Create your models here.
class User(AbstractUser):
    avatar = ImageField(upload_to='users/avatars/')
    register_date = DateTimeField(auto_now_add=True)
    bio = CharField(max_length=256, null=True, blank=True)
