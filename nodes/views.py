from rest_framework import viewsets, status
from rest_framework.response import Response

from trees.models import Tree
from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def create(self, request, *args, **kwargs):
        tree_id = request.data.get('tree_id')
        if not tree_id:
            return Response({'error': 'Tree ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure the tree exists
        try:
            tree = Tree.objects.get(id=tree_id)
        except Tree.DoesNotExist:
            return Response({'error': 'Invalid Tree ID'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with node creation, making sure to link it to the tree
        node = Node.objects.create(tree=tree, person_id=request.data.get('person_id'))
        return Response(NodeSerializer(node).data, status=status.HTTP_201_CREATED)