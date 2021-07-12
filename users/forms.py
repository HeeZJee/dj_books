from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models

CustomUser = get_user_model()

class CustomUserCreationForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('email', 'username')
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('email', 'username')
