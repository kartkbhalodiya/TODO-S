from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    wake_word = models.CharField(max_length=50, default='Hey Nova')
    preferred_language = models.CharField(max_length=10, default='en')
    ai_personality = models.CharField(max_length=20, default='Professional')
    use_local_ai = models.BooleanField(default=False)
    gemini_key = models.CharField(max_length=255, blank=True)
    smart_silence_enabled = models.BooleanField(default=False)
    auto_reply_enabled = models.BooleanField(default=False)
    daily_digest_enabled = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return self.user.username
