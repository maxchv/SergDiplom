from datetimewidget.widgets import DateTimeWidget
from django import forms

from .models import *


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        exclude = ['checked']
        # fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок отзыва'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Содержимое отзыва',
                       'rows': 5}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['client', 'canceled', 'timestamp']

        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'showMeridian': False,
            'startDate': "15/02/2017",
            'minuteStep': 30,
            'daysOfWeekDisabled': [0, 6],
            'weekStart': 1
        }

        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'pattern': '(\+38)?\s*\(?0\d{2}\)?\s*\d{3}\s*[ \-]?\s*(\d{2}\s*[ \-]?\s*){2}',
                    'type': 'tel'
                }
            ),
            'datetime': DateTimeWidget(options=dateTimeOptions,
                                       usel10n=True,
                                       bootstrap_version=3)
        }
