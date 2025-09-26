# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Enquiry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    enquiry_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    status_choices = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('converted', 'Converted'),
        ('lost', 'Lost'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='new')

    def __str__(self):
        return f"{self.name} - {self.status}"