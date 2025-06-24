from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render




class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"Current Balance: {self.current_balance} "

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices=[('CREDIT', 'CREDIT'), ('DEBIT', 'DEBIT')], max_length=6)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.expense_type} - {self.amount} - {self.description} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"