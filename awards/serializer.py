from rest_framework import serializers
from .models import Project,Post

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['sitename', 'Technology', 'url', 'Description', 'image']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'prof_pic', 'bio']