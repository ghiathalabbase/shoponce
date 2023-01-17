from django.urls import path
from DB import views
urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('done/', views.get)
]