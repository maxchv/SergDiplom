from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ClientProfile


class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+38 (0XX) XXX-XX-XX',
                                            'type': 'tel'})
        }


class UserFormView(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Обязательное поле. Только буквы, цифры и символы @/./+/-/_.',
                               widget=forms.TextInput(attrs={'id': 'username-register'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(UserFormView, self).save(commit=False)
        if commit:
            user.save()
        return user
