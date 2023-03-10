from DB.models import Store
from DB.serializers.store_serializers import TopStoresSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

class GetTopStores(APIView):
    def get(self, request, format=None):
        stores_json = []
        stores = Store.objects.order_by('-rate')[:5]
        # for store in stores :
        serialized_store = TopStoresSerializer(stores, many=True)
        return JsonResponse(serialized_store.data, status=status.HTTP_200_OK, safe=False)