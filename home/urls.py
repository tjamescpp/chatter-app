from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='welcome'),
    path('chatter/', include('posts.urls')),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
