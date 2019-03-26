from typing import Any

from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Custom views...

# ViewSet is a view that is used to display serialized model
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewd or edited
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class ApiObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(ApiObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        # context is for obtaining object url so it can build absolute URLs.
        serializer = UserSerializer(user, many=False, context={'request': request})
        return Response({'token': token.key, 'user':serializer.data})