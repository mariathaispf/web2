from django.urls import path
from . import views

urlpatterns = [
    path('sudeste', views.sudeste, name = 'sudeste'),
    path('espirito_santo', views.espirito_santo, name = 'espirito_santo'),
    path('minas_gerais', views.minas_gerais, name = 'minas_gerais'),
    path('', views.voltar, name = 'voltar'),
]