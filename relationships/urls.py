from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelationshipsViewSet

router = DefaultRouter()
router.register('relationships', RelationshipsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]