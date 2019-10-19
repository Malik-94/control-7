from django import forms
from webapp.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option_text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['poll']