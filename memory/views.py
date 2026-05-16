from rest_framework import viewsets, permissions
from .models import Memory
from .serializers import MemorySerializer

class MemoryViewSet(viewsets.ModelViewSet):
    serializer_class = MemorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Memory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
