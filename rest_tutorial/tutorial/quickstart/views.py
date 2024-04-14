from django.shortcuts import render
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from django.contrib.auth.models import Group, User
# Create your views here.

#viewset - type of class based view, no .get() .post(), instead .list() .create()
#modelviewset - subset of viewset, with common corresponding crud 

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')   #orm
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all().order_by('name')   
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]
