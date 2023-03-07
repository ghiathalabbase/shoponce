from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps, loads
from django.contrib.auth import login, logout
from DB.models import User, Profile, Country, City
from django.views import View
from DB.serializers.user_serializers import UserSerializer, ProfileSerializer
from DB.forms.user_forms import CreateUserForm
from django.middleware.csrf import get_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
import uuid

# cache = cache.get("default")

class CSRFView(View):

    def get(self, request):
        token = get_token(request)
        return JsonResponse({'token': token})

class RegisterView(View):

    def post(self, request):
        register_info: dict = loads(request.body)
        user_form = CreateUserForm(data=register_info['user'])
        if user_form.is_valid():
            code = register_info.get('user').get('username').encode('utf-8').hex()
            # cache way
            cache.set(code, register_info, 3600)
            print(code)
            print(cache.get(code))
            #     # session way
            # request.session[code] = register_info
            # request.session.set_expiry(3600 * 48)
            email = EmailMessage(
              subject='Verification Email',
              body="""Hello User, welcome to shoponce.
              Please click on the link below to verify your account:
              http://127.0.0.1:8000/verification?code=%s
              """ % code,
              from_email=settings.EMAIL_HOST_USER,
              to=['ghiathalabbase@gmail.com'],
            )
            is_sent = email.send(fail_silently=False)
            return JsonResponse({
                'message':
                'We sent you a verification email containing a verification link, We need to make sure that this email is yours until we can create your account. "Note: you have two hours to verify your account."'
            })
        else:
            return JsonResponse({'errors': user_form.errors})


class VerificatoinView(View):

    def get(self, request):
        code = self.request.GET.get('code')
        # cache way
        register_info = cache.get(code)
        # session way
        # register_info = request.session.get(code)
        if register_info is not None:
            new_user = User.objects.create(**register_info['user'])
            Profile.objects.create(user=new_user,**register_info['user_profile'])
            login(request, new_user)
            # del request.session[code]
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
        print(self.request.user)
        try:
            user = User.objects.get(username=credentials.get('username'))
        except:
            return JsonResponse('Username Not Found', safe=False)
        password_authenticity: bool = True if credentials.get('password') == user.password else False
        if password_authenticity:
            login(self.request, user)
            serialized_user = UserSerializer(instance=user)
            serialized_profile = ProfileSerializer(instance=Profile.objects.get(user_id=user.id))
            return JsonResponse({** serialized_profile.data, **serialized_user.data,  'is_authenticated': True})
        else:
            return JsonResponse('Wrong Password', safe=False)


# Logout View
class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponse()


# Profile Getter View
class UserProfileView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            serialized_user = UserSerializer(instance=self.request.user)
            serialized_profile = ProfileSerializer(instance=Profile.objects.get(user_id=self.request.user))
            return JsonResponse({**serialized_profile.data, **serialized_user.data,  'is_authenticated': True})
        else:
            if self.request.session.get('info'):
                return JsonResponse({
                    'is_authenticated': False,
                    'registered': True
                })
            else:
                return JsonResponse({'is_authenticated': False})
