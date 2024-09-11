from django.db import models
from trees.models import Tree


class Node(models.Model):
    person = models.OneToOneField('persons.Person', on_delete=models.CASCADE, related_name='node')
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name="nodes")