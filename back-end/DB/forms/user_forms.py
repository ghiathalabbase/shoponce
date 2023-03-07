from django.forms import ModelForm
from DB.models import User, Profile

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
