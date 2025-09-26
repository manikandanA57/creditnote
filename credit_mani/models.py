from django.db import models
from django.utils import timezone

class Customer (models.Model):
    name =models.CharField(max_length=255,editable=True)
    email =models.EmailField()

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100,unique=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class CreditNote(models.Model):
    credit_note_number = models.CharField(max_length=100, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='credit_notes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

def __str__(self):
    return f"credit Note {self.crediot_note_number} for InVoice {self.invoice.invoice_number}"


# Create your models here.
