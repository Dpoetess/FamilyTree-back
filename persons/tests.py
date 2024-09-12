import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from nodes.models import Node
from trees.models import Tree
from .models import Person


@pytest.mark.django_db
class TestPersonViewSet:

    @pytest.fixture
    def user(self):
        return User.objects.create_user(username='testuser', password='testpass')

    @pytest.fixture
    def tree(self, user):
        return Tree.objects.create(name='Family Tree', user=user)

    @pytest.fixture
    def person(self):
        return Person.objects.create(first_name='Harry', last_name='Potter')

    def test_create_person_success(self, client, tree):
        """Test creates a new person successfully."""
        url = reverse('person-list')
        person_data = {
            'first_name': 'Harry',
            'last_name': 'Potter',
            'tree_id': tree.id
        }
        response = client.post(url, person_data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['person']['first_name'] == 'Harry'

    def test_create_person_missing_first_name(self, client):
        """Test fails to create a person without a first name."""
        url = reverse('person-list')
        person_data = {
            'last_name': 'Potter',
            'tree_id': 1
        }
        response = client.post(url, person_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.data
        assert response.data['error'] == 'First name is required.'

    def test_update_person(self, client, person):
        """Test updates a person's data."""
        url = reverse('person-detail', kwargs={'pk': person.pk})
        updated_data = {
            'first_name': 'Harry',
            'last_name': 'Pottersdam',
        }
        response = client.put(url, updated_data, content_type='application/json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['last_name'] == 'Pottersdam'

    def test_delete_person_with_confirmation(self, client, person):
        """Test deletes a person with confirmation."""
        url = reverse('person-detail', kwargs={'pk': person.pk})
        response = client.delete(f"{url}?confirm_delete=true")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Person.objects.filter(pk=person.pk).exists()
