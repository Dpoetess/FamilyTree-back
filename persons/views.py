from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from nodes.models import Node
from nodes.serializers import NodeSerializer
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        # Ensure first_name is provided
        if not request.data.get('first_name'):
            return Response({'error': 'First name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create person first
        person_serializer = self.get_serializer(data=request.data)
        person_serializer.is_valid(raise_exception=True)
        person = person_serializer.save()

        # Create node linked to the person
        tree_id = request.data.get('tree_id')  # Pass the correct tree_id from the request
        node = Node.objects.create(person=person, tree_id=tree_id)

        # Return both person and node details in the response
        return Response({
            'person': person_serializer.data,
            'node': NodeSerializer(node).data
        }, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()