from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # cuando entre a /
    path('iniciosesion/', views.iniciosesion, name='iniciosesion'),  # cuando entre a /iniciosesion/
    path('registro/', views.registro, name='registro'),
    path('crud/', views.crud, name='crud'),
]
