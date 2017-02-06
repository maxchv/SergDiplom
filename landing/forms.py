from django import forms
from .models import *
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        # exclude = ['message', 'phone']
        fields = "__all__"


class UserFormView(UserCreationForm):
    # first_name = forms.CharField(label=_('first name'), max_length=30, required=True)
    # last_name = forms.CharField(label=_('last name'), max_length=30, required=False)
    email = forms.EmailField(label=_("Email address"), required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserFormView, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# http://ustimov.org/posts/17/
class RegisterFormView(FormView):
    form_class = UserFormView

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)