from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import NoteViewSet, SignupView

"""Contains urls for displaying the notes"""

router = DefaultRouter()

router.register(r'notes', NoteViewSet, basename="notes-view")


urlpatterns = [
    path('sign-up/', SignupView.as_view()),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]

