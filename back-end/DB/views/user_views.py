from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps, load
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import check_password
from DB.models import User
from django.views import View
from DB.serializers.user_serializers import UserSerializer, UserFormSerializer
from django.middleware.csrf import get_token
# Create your views here.
# class RegisterView(View):
#   def get(self, request):
#     token = get_token(request)
#     return JsonResponse({'token':token})
#   def post(self, request):
#     register_data : dict = load(request)
#     user_serializer = UserFormSerializer(instance=register_data)
#     if user_serializer.is_valid():
#       new_user = User.objects.create(**register_data)
#       login(request, new_user)
#       ........
      
    

class LoginView(View):
  def get(self, request):
    token = get_token(request)
    return JsonResponse({'token':token})
  def post(self, request):
    credentials = load(request)
    user = None
    try:
      user = User.objects.get(username=credentials.get('username'))
    except:
      return JsonResponse('Username Not Found', safe=False)
    password_authenticity = check_password(password=credentials.get('password'),encoded=user.password)
    if password_authenticity:
      login(request, user)
      serialized_user = UserSerializer(instance=user)
      user = dict(**serialized_user.data)
      user.update(is_authenticated=True)
      return JsonResponse(user)
    else:
      return JsonResponse('Wrong Password', safe=False)
    
# Logout View
class LogoutView(View):
  def get(self, request):
    request.session.delete()
    return HttpResponse()

  
# Profile Getter View 
class UserProfileView(View):
  def get(self,request):
    if request.user.is_authenticated:
      serialized_user = UserSerializer(instance=request.user)
      user = dict(**serialized_user.data)
      user.update(is_authenticated=True)
      return JsonResponse(user)
    else:
      return JsonResponse({'is_authenticated': False})