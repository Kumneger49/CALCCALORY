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
]
