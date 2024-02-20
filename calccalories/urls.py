from django.urls import path
from . import views

app_name='calccalories'
urlpatterns = [
    path('', views.index, name="index"),
    path('/foods', views.foods, name="foods"),
    path('/exercises', views.exercises, name="exercises"),
]
