from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Role, Company
from .serializers import UserSerializer, RoleSerializer, CompanySerializer

# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
