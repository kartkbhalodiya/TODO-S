from django.db import models
from django.contrib.auth.models import User

class FileItem(models.Model):
    TYPE_CHOICES = [('pdf', 'PDF'), ('image', 'Image'), ('video', 'Video'), ('document', 'Document'), ('spreadsheet', 'Spreadsheet'), ('text', 'Text'), ('other', 'Other')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='user_files/')
    file_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='other')
    size = models.IntegerField()
    is_duplicate = models.BooleanField(default=False)
    is_blurry = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
