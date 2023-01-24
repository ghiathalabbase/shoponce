from rest_framework import serializers
from DB.models import Store

class TopStoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'logo', 'rate', 'name')