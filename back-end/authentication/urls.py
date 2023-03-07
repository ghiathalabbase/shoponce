from django.urls import path
from authentication import views
# from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verification', views.VerificatoinView.as_view(), name='verification'),
]