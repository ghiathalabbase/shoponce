from django.urls import path
from DB.views import user_views
from django.views.generic import TemplateView
UserUrls = [
  path('get-csrftoken', user_views.CSRFView.as_view()),
  path('profile', user_views.UserProfileView.as_view(), name='profile'),
  path('',TemplateView.as_view(template_name='DB/i.html')),
  path('stores',TemplateView.as_view(template_name='DB/i.html')),
]