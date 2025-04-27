from django.contrib import admin
from .models import Disciplina, Feedback

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'media_notas')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'aluno', 'nota', 'anonimo', 'criado_em')
    list_filter = ('disciplina', 'anonimo')
    search_fields = ('aluno__username', 'disciplina__nome', 'comentario')
