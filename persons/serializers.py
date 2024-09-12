from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        if not data.get('first_name'):
            raise serializers.ValidationError({"first_name": "First name is required."})
        if not data.get('last_name'):
            raise serializers.ValidationError({"last_name": "Last name is required."})
        return data
