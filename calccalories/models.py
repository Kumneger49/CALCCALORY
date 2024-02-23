from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    weight_in_kg=models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Food(models.Model):
    person=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    person=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

    