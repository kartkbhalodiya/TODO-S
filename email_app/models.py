from django.db import models
from django.contrib.auth.models import User

class EmailAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_accounts')
    provider = models.CharField(max_length=50)  # Gmail, Outlook, Yahoo
    email = models.EmailField()
    is_connected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Email(models.Model):
    PRIORITY_CHOICES = [('urgent', 'Urgent'), ('important', 'Important'), ('normal', 'Normal'), ('low', 'Low')]
    CATEGORY_CHOICES = [('work', 'Work'), ('personal', 'Personal'), ('bills', 'Bills'), ('promotions', 'Promotions'), ('social', 'Social'), ('spam', 'Spam'), ('newsletters', 'Newsletters')]
    account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, related_name='emails')
    from_name = models.CharField(max_length=255)
    from_email = models.EmailField()
    subject = models.CharField(max_length=500)
    body = models.TextField()
    summary = models.TextField(blank=True)
    received_at = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='personal')
    is_read = models.BooleanField(default=False)
    has_attachments = models.BooleanField(default=False)
    reply_draft = models.TextField(blank=True)
    is_fraud = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name='attachments')
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    size = models.IntegerField()
    file = models.FileField(upload_to='attachments/', blank=True, null=True)
    extracted_text = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
