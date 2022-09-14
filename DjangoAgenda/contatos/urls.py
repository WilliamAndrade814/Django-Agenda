from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amigos/', views.amigos, name='amigos'),
    path('familia/', views.familia, name='familia'),
    path('empresa/', views.empresa, name='empresa'),
    path('cadastro/', views.cadastrar_contato, name='cadastrar_contato'),
    path('<int:contato_id>', views.exibir_contato, name='exibir_contato'),
]