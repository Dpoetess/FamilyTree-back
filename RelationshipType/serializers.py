from rest_framework import serializers
from RelationshipType.models import RelationshipType


class RelationshipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipType
        fields = '__all__'