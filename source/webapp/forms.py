from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class EntryForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор')
    mail = forms.EmailField(required=True, label='email')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')

