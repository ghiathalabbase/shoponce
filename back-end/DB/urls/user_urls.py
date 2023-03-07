from django.urls import path
from DB.views import user_views
from django.views.generic import TemplateView
UserUrls = [
  path('get-csrftoken', user_views.CSRFView.as_view()),
  path('login/', user_views.LoginView.as_view(), name='login'),
  path('profile/', user_views.UserProfileView.as_view(), name='profile'),
  path('logout/',user_views.LogoutView.as_view(), name='logout'),
  path('register/', user_views.RegisterView.as_view(), name='register'),
  path('verification', user_views.VerificatoinView.as_view(), name='verification'),
  path('',TemplateView.as_view(template_name='DB/i.html')),
  path('stores',TemplateView.as_view(template_name='DB/i.html')),
]