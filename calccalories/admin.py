from django.contrib import admin
from .models import Person, Food, Exercise

admin.site.register(Person)
admin.site.register(Food)
admin.site.register(Exercise)
# Register your models here.
