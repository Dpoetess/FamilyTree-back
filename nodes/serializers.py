from rest_framework import serializers
from persons.serializers import PersonSerializer
from .models import Node


class NodeSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Node
        fields = '__all__'
