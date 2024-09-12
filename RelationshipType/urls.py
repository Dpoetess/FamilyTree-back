from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelationshipTypeViewSet

router = DefaultRouter()
router.register('relationshiptype', RelationshipTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]