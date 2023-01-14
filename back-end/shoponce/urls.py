"""shoponce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .settings import MEDIA_ROOT, SHOP_MEDIA_URL, PRODUCT_MEDIA_URL, USER_MEDIA_URL 
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(SHOP_MEDIA_URL, document_root=os.path.join(MEDIA_ROOT, SHOP_MEDIA_URL))
urlpatterns += static(PRODUCT_MEDIA_URL, document_root=os.path.join(MEDIA_ROOT, PRODUCT_MEDIA_URL))
urlpatterns += static(USER_MEDIA_URL, document_root=os.path.join(MEDIA_ROOT, USER_MEDIA_URL))
