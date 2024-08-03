from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsProfileOwnerOrReadOnly, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer