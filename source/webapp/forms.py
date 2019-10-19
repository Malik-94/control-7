from django import forms
from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['created_at']

#
# class Form(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields = ['statuses']
