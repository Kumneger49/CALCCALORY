from django import forms
from .models import Exercise

class ExerciseForm(forms.Form):
    minutes=forms.IntegerField()
    
        
    
     