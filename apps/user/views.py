from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from apps.post.models import Post
from apps.user.forms import LoginForm, RegisterForm


# Create your views here.

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'user/home.html', context=context)


class AboutView(View):
    def get(self, request):
        return render(request, 'user/about.html')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.filter(owner=request.user)
        context = {'posts': posts}
        return render(request, 'user/user_posts.html', context=context)


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return render(request, 'user/logout.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'user/login.html', context=context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request=request, username=request.POST.get('username'),
                                password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, 'You are successfully logged in!')
                return redirect('user:home')
            else:
                messages.warning(request, 'Invalid username or password.')
                return redirect('user:login')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'user/register.html', context=context)

    def post(self, request):
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration was successful!')
            return redirect('user:login')
        else:
            context = {'form': form}
            return render(request, 'user/register.html', context=context)
