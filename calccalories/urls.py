from django.urls import path
from . import views

app_name='calccalories'
urlpatterns = [
    path('', views.index, name="index"),
    path('foods', views.foods, name="foods"),
    path('exercises', views.exercises, name="exercises"),
    path('exercise/<int:exercise_id>', views.exercise, name='exercise'),
    path('food/<int:food_id>', views.food, name='food'),
    path('report', views.report, name="report"),
    path('new_food', views.new_food, name="new_food"),
    path('new_exercise', views.new_exercise, name="new_exercise"),
    path('edit_food/<int:food_id>', views.edit_food, name="edit_food"),
    path('edit_exercise/<int:exercise_id>', views.edit_exercise, name="edit_exercise"),
    path('delete_food/<food_id>', views.delete_food, name="delete_food"),
    path('delete_exercise/<exercise_id>', views.delete_exercise, name="delete_exercise"),
]
