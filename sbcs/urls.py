from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('politica/', views.privacidade, name='politica'),
    path('termos/', views.termos, name='termos'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('up_2/', views.up, name='up_2'),

]