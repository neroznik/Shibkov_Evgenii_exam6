from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]

BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class EntryForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, initial='Unknown', label='Автор')
    mail = forms.EmailField(max_length=254, required=True, initial='Unknown', label='email')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)
    updated_at = forms.DateTimeField(required=False, label='Обновлено',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')

