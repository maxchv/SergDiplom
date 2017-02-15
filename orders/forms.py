from datetimewidget.widgets import DateTimeWidget
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
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок отзыва'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Содержимое отзыва'}),
        }


class OrderForm(forms.ModelForm):
    # datetime = forms.DateTimeField(label='Время',input_formats=['%Y-%m-%dT%H:%M'],
    #                                widget=forms.TextInput(attrs={'type':'datetime-local'}))

    class Meta:
        model = Order
        exclude = ['client', 'canceled', 'timestamp']
        #fields = "__all__"

        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'showMeridian': False,
            'startDate': "15/02/2017",
            'minuteStep': 30,
            'daysOfWeekDisabled': [0,6],
            'weekStart': 1
        }

        widgets = {
            'phone': forms.TextInput(
                attrs={'placeholder': '(0XX) XXX-XX-XX'}
            ),
            'datetime': DateTimeWidget(options=dateTimeOptions,
                                       #attrs={'id': "datetime_id"},
                                       usel10n=True,
                                       bootstrap_version=3)
        }
