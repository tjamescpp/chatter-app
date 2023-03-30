from django.urls import path, include

from . import views

urlpatterns = [
    path('posts', views.PostListView.as_view(), name='posts.list'),
    path('new', views.PostCreateView.as_view(), name='posts.new'),
    path('chatrooms', views.ChatroomListView.as_view(), name='chatrooms.list'),
    path('chatrooms/<int:pk>/', views.ChatroomDetailView.as_view(),
         name='chatroom.detail'),
]
