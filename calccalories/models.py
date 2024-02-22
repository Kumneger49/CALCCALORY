from django.db import models

# Create your models here.

class Person(models.Model):
    username=models.CharField(max_length=50)
    weight_in_kg=models.IntegerField(default=0)
    
    def __str__(self):
        return self.username

class Food(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name=models.CharField(max_length=50)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

    