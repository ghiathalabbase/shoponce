from rest_framework import serializers
from DB.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'profile_image', 'email', 'username', 'city', 'favos_products', 'favos_categories', 'favos_tags')
class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'gender', 'profile_image', 'email', 'username', 'city')