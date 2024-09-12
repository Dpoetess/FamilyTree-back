from rest_framework import viewsets
from RelationshipType.models import RelationshipType
from RelationshipType.serializers import RelationshipTypeSerializer


class RelationshipTypeViewSet(viewsets.ModelViewSet):
    queryset = RelationshipType.objects.all()
    serializer_class = RelationshipTypeSerializer