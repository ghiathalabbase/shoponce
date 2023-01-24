from django.urls import path
from DB.urls import user_urls, store_urls

urlpatterns = [
] + user_urls.UserUrls + store_urls.StoreUrls