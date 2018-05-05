from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('up_2/', views.up, name='up_2'),

]