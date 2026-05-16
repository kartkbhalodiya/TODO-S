from rest_framework import viewsets, permissions
from .models import FileItem
from .serializers import FileItemSerializer

class FileItemViewSet(viewsets.ModelViewSet):
    serializer_class = FileItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FileItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
