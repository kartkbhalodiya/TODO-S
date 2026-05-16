from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    CATEGORY_CHOICES = [('important', 'Important'), ('social', 'Social'), ('shopping', 'Shopping'), ('banking', 'Banking'), ('work', 'Work'), ('otp', 'OTP'), ('spam', 'Spam'), ('promotions', 'Promotions'), ('other', 'Other')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    app_name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    body = models.TextField()
    received_at = models.DateTimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_read = models.BooleanField(default=False)
    is_silenced = models.BooleanField(default=False)
    is_auto_action_taken = models.BooleanField(default=False)
    auto_action_type = models.CharField(max_length=50, blank=True)
    package_name = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
