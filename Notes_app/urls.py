from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

"""Contains urls for displaying the notes"""

router = DefaultRouter()

router.register(r'notes', NoteViewSet, basename="notes-view")


urlpatterns = [
    path('', include(router.urls)),
]
