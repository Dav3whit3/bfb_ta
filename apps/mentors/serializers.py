from .models import Mentor, Project, Mentorship
from rest_framework import serializers


class MentorshipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mentorship
        fields = '__all__'

      
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


class MentorSerializer(serializers.ModelSerializer):
    
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = '__all__'
        depth = 1