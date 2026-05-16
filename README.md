# Ex01 Django ORM Web Application
## Date: 16.05.2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)

models.py

from django.db import models
from django.contrib import admin

class Employee(models.Model):
    eid = models.CharField(max_length=20, help_text="Employee")
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'name', 'salary', 'age', 'email')

```


## OUTPUT
![alt text](<Screenshot 2026-05-16 231219.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
