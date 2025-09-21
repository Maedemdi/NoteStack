from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet, SignupView, LoginView

"""Contains urls for displaying the notes"""

router = DefaultRouter()

router.register(r'notes', NoteViewSet, basename="notes-view")


urlpatterns = [
    path('sign-up/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('', include(router.urls)),
]
