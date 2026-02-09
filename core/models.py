import uuid 
from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser, TimeStampedModel):
    department_choices = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('SALES', 'Sales'),
    ]
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=20, choices=department_choices)

    def __str__(self):
        return f"{self.username} - {self.employee_id}"
    
class Asset(TimeStampedModel):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assets')

    def __str__(self):
        return f"{self.name} - {self.serial_number}"
    

    
