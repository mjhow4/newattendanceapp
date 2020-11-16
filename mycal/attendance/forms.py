from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'no',
            'file_number',
            'defendant',
            'complainant',
            'offense',
            'attorney',
            'court_date',
            'plea_request',
            'response_by',
            'defense_name',
            'continuance',
            'disposition',
            'p',
            'a',
            'l',
    ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


