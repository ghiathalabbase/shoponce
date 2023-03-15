from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps, loads
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from DB.models import User, Profile
from django.views import View
from DB.serializers.user_serializers import UserSerializer, ProfileSerializer
from .forms import CreateUserForm
# from django.middleware.csrf import get_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q

TRY_EMAIL = 'ghiathalabbase@gmail.com'

class RegisterView(View):
    def post(self, request):
        errors = {'errors': {}}
        register_info: dict = loads(request.body)
        encoded_email = register_info['user']['email'].encode('utf-8').hex()
        if cache.get(encoded_email) is None:

            user_form = CreateUserForm(data=register_info['user'])

            if  user_form.is_valid():
                cache.set(encoded_email, register_info, 3600)
                print('http://127.0.0.1:8000/auth/verification?code=%s'% encoded_email)

                # email = EmailMessage(
                #     subject='Verification Email',
                #     body="""Hello User, welcome to shoponce.
                #     Please click on the link below to verify your account:
                #     http://127.0.0.1:8000/auth/verification?code=%s
                #     """ % code,
                #     from_email=settings.EMAIL_HOST_USER,
                #     to=[TRY_EMAIL],
                # )
                # try:
                #     is_sent = email.send(fail_silently=False)
                # except Exception as error:
                #     return JsonResponse({'errors': {"email": ["Email is Not Found"]}})
                return JsonResponse({
                    'message':
                    'We sent you a verification email containing a verification link, We need to make sure that this email is yours until we can create your account. "Note: you have two hours to verify your account."'
                })
            errors['errors'] = user_form.errors
            return JsonResponse(errors)
        
        errors['errors']= {'email': ['This email is already taken, use another.']}
        return JsonResponse(errors)

class VerificatoinView(View):
    def get(self, request):
        code = self.request.GET.get('code')
        register_info = cache.get(code)
        if register_info is not None:
            new_user = User.objects.create_user(**register_info['user'])
            Profile.objects.create(user=new_user,**register_info['user_profile'])
            login(request, new_user)
            cache.delete(code)
            return redirect('http://127.0.0.1:5173')
        else:
            response = HttpResponse('Error: this code is not found')
            response.status_code = 404
            return response

class LoginView(View):
    def post(self, request):
        credentials: dict = loads(self.request.body)
        user = None
        try:
            user = User.objects.get(email=credentials.get('email'))
        except:
            return JsonResponse('Email Not Found', safe=False)
        password_authenticity: bool = check_password(credentials.get('password'), user.password)
        if password_authenticity:
            login(self.request, user)
            serialized_user = UserSerializer(instance=user)
            serialized_profile = ProfileSerializer(instance=Profile.objects.get(user_id=user.id))
            return JsonResponse({** serialized_profile.data, **serialized_user.data,  'is_authenticated': True})
        else:
            return JsonResponse('Wrong Password', safe=False)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse()
