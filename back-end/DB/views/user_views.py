from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from json import dumps, loads
from DB.models import Profile, Country, City
from django.views import View
from DB.serializers.user_serializers import UserSerializer, ProfileSerializer
from django.middleware.csrf import get_token

class CSRFView(View):

    def get(self, request):
        token = get_token(request)
        return JsonResponse({'token': token})

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
