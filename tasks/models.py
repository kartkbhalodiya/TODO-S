from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [('urgent', 'Urgent'), ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]
    STATUS_CHOICES = [('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    category = models.CharField(max_length=100, default='General')
    tags = models.JSONField(default=list, blank=True)
    is_recurring = models.BooleanField(default=False)
    recurring_rule = models.CharField(max_length=100, blank=True)
    estimated_minutes = models.IntegerField(default=30)
    is_ai_suggested = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
