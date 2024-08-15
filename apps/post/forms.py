from django.forms import *

from apps.post.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['owner']
        fields = '__all__'

    def save(self, user, commit=True):
        post = super().save(commit=False)
        post.owner = user
        post.save()
        return post
