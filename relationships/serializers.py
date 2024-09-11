from rest_framework import serializers
from relationships.models import Relationships


class RelationshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationships
        fields = '__all__'