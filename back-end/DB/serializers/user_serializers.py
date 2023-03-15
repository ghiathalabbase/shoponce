from rest_framework import serializers
from DB.models import Profile
from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    class Meta: 
        model = Profile
        fields = ('name','country', 'city', 'profile_image', 'favo_products', 'favo_categories', 'favo_tags')