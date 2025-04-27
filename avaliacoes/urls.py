from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_disciplinas, name='lista_disciplinas'),
    path('<int:id>/', views.detalhes_disciplina, name='detalhes_disciplina'),
    path('<int:id>/avaliar/', views.avaliar_disciplina, name='avaliar_disciplina'),
    path('feedback/<int:id>/editar/', views.editar_feedback, name='editar_feedback'),
    path('feedback/<int:id>/excluir/', views.excluir_feedback, name='excluir_feedback'),
]
