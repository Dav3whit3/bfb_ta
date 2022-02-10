from .models import Mentor, Project, Mentorship
from rest_framework import serializers


class MentorshipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mentorship
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'mentors']
        depth = 1


# This extra Serializer will only serve to be nested in Mentors'
# responses and not show again an unnecesary "mentors" field inside
class NestedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name',]


class MentorSerializer(serializers.ModelSerializer):
    
    projects = NestedProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = ['id', 'name', 'gender', 'email', 'projects']
