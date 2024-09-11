from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from trees.models import Tree
from trees.serializers import TreeSerializer


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        default_user = User.objects.get(id=1)  # Replace with the default user logic
        serializer.save(user=default_user)