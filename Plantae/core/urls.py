
# core/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('consultar/', views.listar_plantas, name='consultar'),
    path('sobre/', views.about, name='sobre'),
    path('criar/', views.criar, name='criar_plantas'),
    path('editar/<str:nome_planta>/', views.editar, name='editar_planta'),
    path('excluir/<str:nome_planta>/', views.excluir, name='excluir_planta'),
]
