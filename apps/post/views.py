from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from apps.post.forms import PostForm
from apps.post.models import Post


# Create your views here.

class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'post/post_form.html', context=context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(user=request.user)
            post.save()
            messages.success(request, 'Your post has been saved.')
            return redirect('user:profile')
        else:
            form = PostForm()
            context = {'form': form}
            return render(request, 'post/post_form.html', context=context)


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {
            'post': post,
            'request_user': request.user
        }
        return render(request, 'post/post_detail.html', context)


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        context = {'post': post, 'form': form}
        return render(request, 'post/post_form.html', context)

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(user=request.user)
            post.save()
            messages.success(request, 'Your post has been updated.')
            return redirect('user:profile')
        else:
            context = {'post': post, 'form': form}
            return render(request, 'post/post_form.html', context)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('user:home')
