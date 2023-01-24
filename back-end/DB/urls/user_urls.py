from django.urls import path
from DB.views import user_views
UserUrls = [
  path('login/', user_views.LoginView.as_view(), name='login'),
  path('profile/', user_views.UserProfileView.as_view(), name='profile'),
  path('logout/',user_views.LogoutView.as_view(), name='logout')
  # path('check/', views.check),
]