from rest_framework import serializers
from .models import Profile, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['sitename', 'url', 'Description', 'image']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'prof_pic', 'bio']