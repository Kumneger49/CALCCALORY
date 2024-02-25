from django.urls import path
from . import views

app_name='calccalories'
urlpatterns = [
    path('', views.index, name="index"),
    path('foods', views.foods, name="foods"),
    path('exercises', views.exercises, name="exercises"),
    path('exercise/<int:exercise_id>', views.exercise.as_view(), name='exercise'),
    path('food/<int:food_id>', views.food.as_view(), name='food'),
    path('report', views.report, name="report"),
    path('new_food', views.new_food.as_view(), name="new_food"),
    path('new_exercise', views.new_exercise.as_view(), name="new_exercise"),
    path('edit_food/<int:food_id>', views.edit_food.as_view(), name="edit_food"),
    path('edit_exercise/<int:exercise_id>', views.edit_exercise.as_view(), name="edit_exercise"),
    path('check_delete_food/<food_id>', views.check_delete_food, name='check_delete_food'),
    path('do_not_delete_food/<food_id>', views.do_not_delete_food, name='do_not_delete_food'),
    path('delete_food/<food_id>', views.delete_food, name="delete_food"),
    path('check_delete_exercise/<exercise_id>', views.check_delete_exercise, name='check_delete_exercise'),
    path('do_not_delete_exercise/<exercise_id>', views.do_not_delete_exercise, name='do_not_delete_exercise'),
    path('delete_exercise/<exercise_id>', views.delete_exercise, name="delete_exercise"),
]
