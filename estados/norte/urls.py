from django.urls import path
from . import views

urlpatterns = [
    path('norte', views.norte, name = 'norte'),
    path('amazonas', views.amazonas, name = 'amazonas'),
    path('para', views.para, name = 'para'),
    path('tocantins', views.tocantins, name = 'tocantins'),
    path('', views.voltar, name = 'voltar'),
]