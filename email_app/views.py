from rest_framework import viewsets, permissions
from .models import EmailAccount, Email
from .serializers import EmailAccountSerializer, EmailSerializer

class EmailAccountViewSet(viewsets.ModelViewSet):
    serializer_class = EmailAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EmailAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Email.objects.filter(account__user=self.request.user)

    def perform_create(self, serializer):
        account = serializer.validated_data.get('account')
        if account is None:
            account, _ = EmailAccount.objects.get_or_create(
                user=self.request.user,
                provider='Local',
                email=self.request.user.email or f'{self.request.user.username}@local.nova',
                defaults={'is_connected': True},
            )
        serializer.save(account=account)
