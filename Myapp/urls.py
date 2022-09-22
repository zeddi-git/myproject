from django.urls import path  #allows us to add multiple urls in a list

from . import views  #this imports the views function

urlpatterns = [
    path('', views.index, name= 'index'),
    path('counter', views.counter, name= 'counter'),
    path('register',views.register, name = 'register')
]

