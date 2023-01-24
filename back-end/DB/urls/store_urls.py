from django.urls import path
from DB.views import store_views

StoreUrls = [
    path('store/get-top/',store_views.GetTopStores.as_view()),
]