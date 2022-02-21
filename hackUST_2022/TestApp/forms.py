from django import forms
from .models import *

class PeopleRegistrationForm(forms.ModelForm):

    class Meta:
        model = People
        fields = ['name','email','age','teacher','food','school','slug','image']

