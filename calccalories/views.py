from django.shortcuts import render
from .models import Food, Exercise

def index(request):
    return render(request, 'calccalories/index.html')

def foods(request):
    foods=Food.objects.all()
    context={'foods': foods}
    return render(request, 'calccalories/foods.html', context)

def exercises(request):
    exercises=Exercise.objects.all()
    context={'exercises': exercises}
    return render(request, 'calccalories/exercises.html', context)

# Create your views here.
