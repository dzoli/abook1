from django.contrib.auth.models import User, Group
from rest_framework import serializers


# HyperlinkModelSerializer is a serializer for built-in models
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
