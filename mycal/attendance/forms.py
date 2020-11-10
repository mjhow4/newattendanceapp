from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'no',
            'file_number',
            'defendant_name',
            'complainant',
            'offense',
            'attorney',
            'plea_request',
        
    ]
       
