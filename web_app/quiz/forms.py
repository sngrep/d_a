from .models import Choices, Attempt
from django import forms


class AttemptForm(forms.ModelForm):

    class Meta:
        model = Attempt
        fields = ('username', 'name',)


class ChoicesForm(forms.ModelForm):

    class Meta:
        model = Choices
        fields = ('related_attempt', 'question', 'answer_true',)
