from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,Profile

class PostSerializer(serializers.ModelSerializer):