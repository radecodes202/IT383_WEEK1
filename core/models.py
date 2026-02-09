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
    

class Organization(TimeStampedModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class LeaveRequest(TimeStampedModel):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests')    
    reason = models.TextField()
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approvals')
    is_approved = models.BooleanField(default=False)
    
class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    stock_qty = models.IntegerField(default=0)

class Warehouse(TimeStampedModel):
    location = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='StockMovement')

class StockMovement(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text='Positive to add, negative to remove')
    movement_type = models.CharField(max_length=20, choices=[('IN', 'IN'), ('OUT', 'OUT')])    
    notes = models.TextField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.movement_type == 'IN':
            self.product.stock_qty += self.quantity
        elif self.movement_type == 'OUT':
            self.product.stock_qty -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

        
    
