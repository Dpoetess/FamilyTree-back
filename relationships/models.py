from django.db import models
from persons.models import Person
from RelationshipType.models import RelationshipType
from trees.models import Tree


class Relationships(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    from_person = models.ForeignKey(Person, related_name='from_person', on_delete=models.CASCADE)
    to_person = models.ForeignKey(Person, related_name='to_person', on_delete=models.CASCADE)
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_person} - {self.relationship_type} - {self.to_person}"

