from rest_framework import viewsets
from relationships.models import Relationships
from relationships.serializers import RelationshipsSerializer


class RelationshipsViewSet(viewsets.ModelViewSet):
    queryset = Relationships.objects.all()
    serializer_class = RelationshipsSerializer
