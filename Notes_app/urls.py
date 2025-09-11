from django.urls import path, include
from .views import NoteViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'notes', NoteViewSet, basename="notes-view")

urlpatterns = [
    path('', include(router.urls)),
]
