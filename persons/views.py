from rest_framework import viewsets, status, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from nodes.models import Node
from nodes.serializers import NodeSerializer
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        if not request.data.get('first_name'):
            return Response({'error': 'First name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        person_serializer = self.get_serializer(data=request.data)
        if person_serializer.is_valid(raise_exception=True):
            person = person_serializer.save()

            tree_id = request.data.get('tree_id')
            existing_node = Node.objects.filter(person=person, tree_id=tree_id).first()

            if existing_node:
                return Response({
                    'error': 'Node already exists for this person in this tree.',
                    'node': NodeSerializer(existing_node).data,
                    'person': person_serializer.data,
                }, status=status.HTTP_400_BAD_REQUEST)

            if not tree_id:
                return Response({'error': 'Tree ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

            node = Node.objects.create(person=person, tree_id=tree_id)

            response_data = {
                'person': person_serializer.data,
                'node': NodeSerializer(node).data
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        data = request.data.copy()

        if 'first_name' not in data:
            data['first_name'] = instance.first_name
        if 'last_name' not in data:
            data['last_name'] = instance.last_name

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        person = self.get_object()

        confirm_delete = request.query_params.get('confirm_delete', None)
        if confirm_delete is None:
            return Response(
                {
                    "message": f"Are you sure you want to delete {person.first_name} {person.last_name}?",
                    "person": PersonSerializer(person).data,  # Send person's details
                    "confirmation": "Pass 'confirm_delete=true' to confirm."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if confirm_delete == 'true':
            person.delete()
            return Response({"message": "Person deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Delete request not confirmed."}, status=status.HTTP_400_BAD_REQUEST)