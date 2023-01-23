from django.urls import path
from DB.all_views.store_views import GetTopStores

StoreUrls = [
    path('store/get-top/', GetTopStores.as_view()),
]