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
    ]

# class DefenseForm(forms.ModelForm):
#     class Meta:
#         model = Defense
#         fields = [
#             'defense_name',
#             'continuance',
#             'plea',
        
#     ]
