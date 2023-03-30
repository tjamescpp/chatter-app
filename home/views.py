from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from posts import models

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/chatter/posts'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(generic.TemplateView):
    template_name = 'home/welcome.html'
