from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    TYPE_CHOICES = [('time', 'Time'), ('location', 'Location'), ('habit', 'Habit'), ('predictive', 'Predictive')]
    STATUS_CHOICES = [('active', 'Active'), ('snoozed', 'Snoozed'), ('completed', 'Completed'), ('dismissed', 'Dismissed')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    reminder_time = models.DateTimeField(blank=True, null=True)
    reminder_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='time')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    location_address = models.CharField(max_length=500, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    radius_meters = models.FloatField(blank=True, null=True)
    habit_name = models.CharField(max_length=100, blank=True)
    is_recurring = models.BooleanField(default=False)
    recurring_rule = models.CharField(max_length=100, blank=True)
    snooze_history = models.JSONField(default=list, blank=True)
    source_app = models.CharField(max_length=100, blank=True)
    is_ai_predicted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
