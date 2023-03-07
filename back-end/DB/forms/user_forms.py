from django.forms import ModelForm
from DB.models import Profile
from authentication.models import User

class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
