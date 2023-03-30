from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from .models import Post, Chatroom
from django.utils import timezone
from .forms import PostsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from . import urls
from django import template

# Create your views here.


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts_list'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.posts.all().order_by('-pub_date')


class ChatroomListView(generic.ListView):
    model = Chatroom
    template_name = 'posts/chatroom_list.html'
    context_object_name = 'chatrooms_list'


class ChatroomDetailView(generic.DetailView):
    model = Chatroom
    template_name = 'posts/chatroom_detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostsForm
    success_url = '/chatter/posts'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
