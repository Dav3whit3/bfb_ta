from .models import Mentor, Project, Mentorship
from rest_framework import serializers

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor
        fields = ['_id', 'name', 'gender', 'email']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['_id', 'name']


class MentorshipSerializer(serializers.HyperlinkedModelSerializer):
    mentors = MentorSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Mentorship
        depth = 1
        fields = '__all__'