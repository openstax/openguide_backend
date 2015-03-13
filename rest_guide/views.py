from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows themes to be viewed or edited
    """
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ElementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elements to be viewed or edited
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

