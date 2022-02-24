from django import http
from django.shortcuts import render
from .models import Mentor, Project , Mentorship
from .serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer, NestedProjectSerializer

from rest_framework import viewsets, permissions


# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):

    # API endpoint that allows projects to be viewed or edited.

    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options', 'trace']


class MentorViewSet(viewsets.ModelViewSet):

    # API endpoint that allows mentors to be viewed or edited.

    queryset = Mentor.objects.all().order_by('id')
    serializer_class = MentorSerializer
    # permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options', 'trace']


class MentorshipViewSet(viewsets.ModelViewSet):

    # API endpoint that allows mentors to be viewed or edited.

    queryset = Mentorship.objects.all().order_by('id')
    serializer_class = MentorshipSerializer
    # permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options', 'trace']

