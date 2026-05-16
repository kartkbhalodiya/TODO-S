from django.db import models
from django.contrib.auth.models import User

class Automation(models.Model):
    TRIGGER_CHOICES = [('battery', 'Battery Level'), ('location', 'Location'), ('time', 'Time'), ('wifi', 'WiFi'), ('bluetooth', 'Bluetooth'), ('app_opened', 'App Opened'), ('notification', 'Notification'), ('email', 'Email'), ('day_of_week', 'Day of Week')]
    ACTION_CHOICES = [('silent_mode', 'Silent Mode'), ('open_app', 'Open App'), ('send_notification', 'Send Notification'), ('adjust_brightness', 'Adjust Brightness'), ('enable_wifi', 'Enable WiFi'), ('enable_bluetooth', 'Enable Bluetooth'), ('play_sound', 'Play Sound'), ('send_email', 'Send Email'), ('create_reminder', 'Create Reminder')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='automations')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    trigger = models.CharField(max_length=50, choices=TRIGGER_CHOICES)
    trigger_value = models.CharField(max_length=200)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    action_value = models.CharField(max_length=200)
    is_enabled = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    execution_count = models.IntegerField(default=0)
    last_executed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
