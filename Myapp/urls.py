from django.urls import path  #allows us to add multiple urls in a list

from . import views  #this imports the views function

urlpatterns = [
    path('', views.index, name= 'index'),
    path('counter', views.counter, name= 'counter'),
    path('register',views.register, name = 'register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name= 'logout'),
    path('post/<str:pk>', views.post, name= 'post')
]

