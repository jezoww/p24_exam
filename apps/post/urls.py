from django.urls import path

from apps.post.views import NewPostView, PostDetailView, PostUpdateView, DeletePostView

app_name = 'post'
urlpatterns = [
    path('create_post/', NewPostView.as_view(), name='create_post'),
    path('post_detail/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path('edit_post/<pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('delete_post/<pk>/', DeletePostView.as_view(), name='delete_post'),
]
