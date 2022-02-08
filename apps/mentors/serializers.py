from .models import Mentor, Project
from rest_framework import serializers

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'gender', 'email']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

