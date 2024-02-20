from django.db import models

# Create your models here.

class Person(models.Model):
    username=models.CharField(max_length=200)
    weight_in_kg=models.IntegerField(default=0)
    
    def __str__(self):
        return self.username

class Food(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    name=models.TextField(max_length=200)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name=models.CharField(max_length=300)
    calory=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

    