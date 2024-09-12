# Generated by Django 5.1.1 on 2024-09-11 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RelationshipType', '0001_initial'),
        ('persons', '0001_initial'),
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_person', to='persons.person')),
                ('relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RelationshipType.relationshiptype')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_person', to='persons.person')),
                ('tree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trees.tree')),
            ],
        ),
    ]
