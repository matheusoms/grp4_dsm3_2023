
# core/urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),  # Adicione esta linha para a URL raiz
    path('consultar/', views.listar_pessoas, name='consultar'),
    path('sobre/', views.about, name='sobre'),
    path('criar/', views.criar, name='criar_pessoa'),
    path('editar/<str:pessoa_cpf>/', views.editar, name='editar_pessoa'),
    path('excluir/<str:pessoa_cpf>/', views.excluir, name='excluir_pessoa'),
]
