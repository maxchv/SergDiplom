from django import forms
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        #exclude = ['message', 'phone']
        fields = "__all__"


# http://ustimov.org/posts/17/
class RegisterFormView(FormView):
    form_class = UserCreationForm

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