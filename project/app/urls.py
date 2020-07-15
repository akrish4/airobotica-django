from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
  path('',views.index,name='index'),
  path('contact',views.contact,name='contact'),
  path('signup',views.handleSignup,name='handleSignup'),
  path('login',views.handleLogin,name='handleLogin'),
  path('handlelogout',views.handlelogout,name='handlelogout'),
  path('handleFriendsBlog',views.friends,name='friends'),
  path('handleBlog',views.handleBlog,name='handleBlog'),
  path('about',views.about,name='about')
]
