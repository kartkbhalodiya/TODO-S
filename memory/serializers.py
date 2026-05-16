from rest_framework import serializers
from .models import Memory

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'last_accessed']
