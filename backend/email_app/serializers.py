from rest_framework import serializers
from .models import EmailAccount, Email, Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
        read_only_fields = ['id']

class EmailSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {'account': {'required': False}}

class EmailAccountSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True, read_only=True)

    class Meta:
        model = EmailAccount
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']
