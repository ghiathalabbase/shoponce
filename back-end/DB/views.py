from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate,login
from .models import User
# Create your views here.
def login_view(request):
  get_token(request)
  if request.method == 'GET':
    return render(request, 'DB/i.html')
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
      user = User.objects.get(username=username)
    except:
      return render(request, 'DB/i.html', {'Error': 'Username Not Found'})
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
    else:
      return render(request, 'DB/i.html', {'Error': 'Wrong Password'})
    return HttpResponse(f'Welcome {user.username}')

def get(request):
  if request.method=='GET':
    get_token(request)
  if request.method=='POST':
    return HttpResponse(dumps('success'))
    
  return HttpResponse(dumps('done'))
