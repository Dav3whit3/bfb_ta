from .models import Mentor, Project, Mentorship
from rest_framework import serializers

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    hashtags = serializers.CharField()
    class Meta:
        model = Mentor
        depth = 1
        fields = '__all__'


class MentorshipSerializer(serializers.HyperlinkedModelSerializer):
    _id_project = MentorSerializer(many=True, read_only=True)
    class Meta:
        model = Mentorship
        depth = 1
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    _id = serializers.IntegerField()
    _id = MentorshipSerializer(many=True, read_only=True)
    title = serializers.CharField()
    class Meta:
        model = Project
        fields = '__all__'
