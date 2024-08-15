from django.db.models import *

from apps.user.models import User


# Create your models here.

class Post(Model):
    title = CharField(max_length=100)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    owner = ForeignKey(User, on_delete=CASCADE)
