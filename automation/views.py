from rest_framework import viewsets, permissions
from .models import Automation
from .serializers import AutomationSerializer

class AutomationViewSet(viewsets.ModelViewSet):
    serializer_class = AutomationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Automation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
