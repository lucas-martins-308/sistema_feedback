from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Disciplina, Feedback
from .forms import FeedbackForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'home.html', {'disciplinas': disciplinas})

@login_required
def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas/lista.html', {'disciplinas': disciplinas})

@login_required
def detalhes_disciplina(request, id):
    disc = get_object_or_404(Disciplina, id=id)
    feedbacks = Feedback.objects.filter(disciplina=disc)
    return render(request, 'disciplinas/detalhes.html', {'disciplina': disc, 'feedbacks': feedbacks})

@login_required
def avaliar_disciplina(request, id):
    disc = get_object_or_404(Disciplina, id=id)
    if Feedback.objects.filter(disciplina=disc, aluno=request.user).exists():
        return redirect('detalhes_disciplina', id=id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.disciplina = disc
            fb.aluno = request.user
            fb.save()
            return redirect('detalhes_disciplina', id=id)
    else:
        form = FeedbackForm()
    return render(request, 'disciplinas/avaliar.html', {'form': form, 'disciplina': disc})

@login_required
def editar_feedback(request, id):
    fb = get_object_or_404(Feedback, id=id)
    if fb.aluno != request.user:
        return redirect('detalhes_disciplina', id=fb.disciplina.id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=fb)
        if form.is_valid():
            form.save()
            return redirect('detalhes_disciplina', id=fb.disciplina.id)
    else:
        form = FeedbackForm(instance=fb)
    return render(request, 'disciplinas/editar_feedback.html', {'form': form, 'feedback': fb})

@login_required
def excluir_feedback(request, id):
    fb = get_object_or_404(Feedback, id=id)
    if fb.aluno == request.user:
        fb.delete()
    return redirect('detalhes_disciplina', id=fb.disciplina.id)
