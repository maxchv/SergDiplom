from django import forms
from .models import *
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class FeedBackForm(forms.ModelForm):

    class Meta:
        model = FeedBack
        exclude = ['checked']
        #fields = "__all__"
