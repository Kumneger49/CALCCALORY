from django import forms
from .models import Exercise, Food

class ExerciseForm(forms.Form):
    minutes=forms.IntegerField()
   
class NewFoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields=['name', 'calory'] 
        labels={'name': 'Enter the name of the food: ', 'calory': "Enter the food's calory: "}
    
class NewExerciseForm(forms.ModelForm):
    class Meta:
        model=Exercise
        fields=['name', 'calory']
        labels={'name': 'Enter the name of the exercise: ', 'calory':"Enter the calory burn per minute for the exercise: "}
 
        
    
     