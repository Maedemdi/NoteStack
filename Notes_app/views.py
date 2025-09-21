from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .models import Note
from .serializers import NoteSerializer, SignUpSerializer, LoginSerializer
from .permissions import UpdateOwnNote


class NoteViewSet(viewsets.ModelViewSet):
    """Enables displaying the notes, with tag-filtering and search features"""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('tags',)
    search_fields = ('title', 'text', 'tags__caption',
                     'user__username', 'user__first_name', 'user__last_name')
    permission_classes = (IsAuthenticatedOrReadOnly, UpdateOwnNote)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SignupView(APIView):
    """Sign-up view"""

    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """Login view"""

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token = Token.objects.get(user=user)

        return Response({
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        }, status=status.HTTP_200_OK)
