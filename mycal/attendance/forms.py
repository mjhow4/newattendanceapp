from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'case_number',
            'attorney',
            'court_session',
            'plea_request',
        ]
       
