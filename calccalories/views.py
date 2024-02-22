from django.shortcuts import render, redirect
from .models import Food, Exercise
from .forms import ExerciseForm
sum=0
sum1=0

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

def exercise(request, exercise_id):
    exercise=Exercise.objects.get(id=exercise_id)
    if request.method!='POST':
        form=ExerciseForm()
        value=0
    else:
        form=ExerciseForm(request.POST)
        if form.is_valid():
            value=form.cleaned_data['minutes']*exercise.calory
            global sum
            sum+=value
            # print(int(request.POST['minutes'])/10, request.user.username)
            return redirect('calccalories:exercises')
    context={'form': form, 'exercise': exercise, 'sum': sum}
    return render(request, 'calccalories/exercise.html', context)


def food(request, food_id):
    food=Food.objects.get(id=food_id)
    if request.method!='POST':
        form=ExerciseForm()
        value=0
    else:
        form=ExerciseForm(request.POST)
        if form.is_valid():
            value=form.cleaned_data['minutes']*food.calory
            global sum1
            sum1+=value
            return redirect('calccalories:foods')
    context={'form': form, 'food': food, 'sum': sum1}
    return render(request, 'calccalories/food.html', context)

def report(request):
    global sum, sum1
    sum=sum-sum1
    context={'sum': sum}
    sum=0
    sum1=0
    return render(request, 'calccalories/report.html', context)
    
    
        
 
