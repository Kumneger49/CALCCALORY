from django.shortcuts import render, redirect
from .models import Food, Exercise
from .forms import ExerciseForm, FoodForm, NewExerciseForm, NewFoodForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
sum=0
sum1=0

def confirm_user(model, request):
    if model.person!=request.user:
        raise Http404

def index(request):
    return render(request, 'calccalories/index.html')

@login_required
def foods(request):
    foods=Food.objects.filter(person=request.user)
    context={'foods': foods}
    return render(request, 'calccalories/foods.html', context)

@login_required
def exercises(request):
    # exercises=Exercise.objects.all()
    exercises=Exercise.objects.filter(person=request.user)
    context={'exercises': exercises}
    return render(request, 'calccalories/exercises.html', context)

@login_required
def exercise(request, exercise_id):
    exercise=Exercise.objects.get(id=exercise_id)
    confirm_user(exercise, request)
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
            new_exercise=form.save(commit=False)
            new_exercise.person=request.user
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
            new_food.person=request.user
            form.save()
            return redirect('calccalories:foods')
    context={'form':form}
    return render(request, 'calccalories/new_food.html', context)

@login_required
def food(request, food_id):
    food=Food.objects.get(id=food_id)
    confirm_user(food, request)
    if request.method!='POST':
        form=FoodForm()
        value=0
    else:
        form=FoodForm(request.POST)
        if form.is_valid():
            value=form.cleaned_data['Units']*food.calory
            global sum1
            sum1+=value
            return redirect('calccalories:foods')
    context={'form': form, 'food': food, 'sum': sum1}
    return render(request, 'calccalories/food.html', context)

@login_required
def edit_food(request, food_id):
    food=Food.objects.get(id=food_id)
    confirm_user(food, request)
    if request.method!='POST':
        form=NewFoodForm(instance=food)
    else:
        form=NewFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('calccalories:foods')
    context={'form':form, 'food':food}
    return render(request, 'calccalories/edit_food.html', context)

@login_required
def edit_exercise(request, exercise_id):
    exercise=Exercise.objects.get(id=exercise_id)
    confirm_user(exercise, request)
    if request.method!='POST':
        form=NewExerciseForm(instance=exercise)
    else:
        form=NewExerciseForm(instance=exercise, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('calccalories:exercises')
    context={'form':form, 'exercise':exercise}
    return render(request, 'calccalories/edit_exercise.html', context)

@login_required
def delete_food(request, food_id):
    food=Food.objects.get(id=food_id)
    food.delete()
    return redirect('calccalories:foods')

@login_required
def delete_exercise(request, exercise_id):
    food=Exercise.objects.get(id=exercise_id)
    food.delete()
    return redirect('calccalories:exercises')

@login_required
def report(request):
    global sum, sum1
    sum=sum-sum1
    context={'sum': sum}
    sum=0
    sum1=0
    return render(request, 'calccalories/report.html', context)
    
    
        
 
