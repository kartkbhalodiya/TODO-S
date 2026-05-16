from django.db import models
from django.contrib.auth.models import User

class Memory(models.Model):
    CATEGORY_CHOICES = [('habit', 'Habit'), ('preference', 'Preference'), ('fact', 'Fact'), ('routine', 'Routine'), ('schedule', 'Schedule'), ('contact', 'Contact'), ('location', 'Location'), ('app_usage', 'App Usage')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memories')
    key = models.CharField(max_length=200)
    value = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='habit')
    confidence = models.FloatField(default=1.0)
    access_count = models.IntegerField(default=0)
    is_synced = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)
