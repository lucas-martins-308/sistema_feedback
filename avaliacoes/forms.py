from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nota', 'comentario', 'anonimo']
        widgets = {
            'nota': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
