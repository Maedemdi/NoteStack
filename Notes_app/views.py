from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token

from .models import Note, NoteStackUser
from .serializers import NoteSerializer, SignUpSerializer

"""Views to enable displaying the notes. With tag-filtering and search features"""


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('tags',)
    search_fields = ('title','text','tags__caption', 'user__username', 'user__first_name', 'user__last_name')
    

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
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


# class NoteStackUserViewSet(viewsets.ModelViewSet):
#     queryset = NoteStackUser.objects.all()
#     serializer_class = NoteStackUserSeriazlizer
#     authentication_classes = (TokenAuthentication,)

    

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
    