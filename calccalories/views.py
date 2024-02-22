from django.shortcuts import render, redirect
from .models import Food, Exercise, Person
from .forms import ExerciseForm, NewExerciseForm, NewFoodForm
from django.contrib.auth.decorators import login_required
sum=0
sum1=0


def index(request):
    return render(request, 'calccalories/index.html')

@login_required
def foods(request):
    # user=Person.objects.get(username=request.user)
    # food.person=user
    # foods=Food.objects.filter(person=request.user)
    foods=Food.objects.all()
    context={'foods': foods}
    return render(request, 'calccalories/foods.html', context)

@login_required
def exercises(request):
    exercises=Exercise.objects.all()
    context={'exercises': exercises}
    return render(request, 'calccalories/exercises.html', context)

@login_required
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

@login_required
def new_exercise(request):
    if request.method!='POST':
        form=NewExerciseForm()
    else:
        form=NewExerciseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('calccalories:exercises')
    context={'form':form}
    return render(request, 'calccalories/new_exercise.html', context)

@login_required
def new_food(request):
    if request.method!='POST':
        form=NewFoodForm()
    else:
        form=NewFoodForm(data=request.POST)
        if form.is_valid():
            new_food=form.save(commit=False)
            user=Person.objects.get(username=request.user)
            new_food.person=user
            form.save()
            return redirect('calccalories:foods')
    context={'form':form}
    return render(request, 'calccalories/new_food.html', context)

@login_required
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

@login_required
def report(request):
    global sum, sum1
    sum=sum-sum1
    context={'sum': sum}
    sum=0
    sum1=0
    return render(request, 'calccalories/report.html', context)
    
    
        
 
