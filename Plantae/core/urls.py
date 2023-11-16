
# core/urls.py
from django.urls import path
from .views import criar, listar_pessoas, editar, excluir


urlpatterns = [
    path('', listar_pessoas, name='home'),  # Adicione esta linha para a URL raiz
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar, name='criar_pessoa'),
    path('editar/<str:pessoa_id>/', editar, name='editar_pessoa'),
    path('excluir/<str:pessoa_id>/', excluir, name='excluir_pessoa'),
]
