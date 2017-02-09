from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(blank=True,
                             max_length=40,
                             verbose_name='Телефон',
                             validators=[
                                 RegexValidator(
                                     regex='(\+38)?\s*\(?0\d{2}\)?\s*\d{3}\s*[ \-]?\s*(\d{2}\s*[ \-]?\s*){2}',
                                     message='Введите телефонный номер в корректном формате (0XX) XXX-XX-XX'
                                 )
                             ])
    photo = models.ImageField(blank=True, verbose_name="Аватарка", upload_to="clients")


# class Client(models.Model):
#     id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     email = models.EmailField()
#     first_name = models.CharField(max_length= 100, verbose_name= 'имя')
#     middle_name = models.CharField(max_length= 100, verbose_name='отчество')
#     last_name = models.CharField(max_length= 100, verbose_name= 'фамилия')
#     phone = models.CharField(max_length=50, verbose_name='телефон')
#     message = models.TextField(max_length= 500, blank=True, verbose_name='сообщение')
#     master=models.ForeignKey('Master')
#
#     def __str__(self):
#         return "Пользователь: %s почта: %s" % (self.first_name, self.email)
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'


class Master(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=' фио мастера')
    contact_phone = models.CharField(max_length=20, verbose_name='контактный телефон')
    master_photo = models.ImageField(upload_to="landing", verbose_name=("фото мастера"), blank=True)

    # client = models.ForeignKey(Client)

    def __str__(self):
        return "Мастер:  %s; " "  тел: %s" % (self.full_name, self.contact_phone)

    class Meta:
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'


class Work_Time(models.Model):
    start_work_day = models.DateTimeField(verbose_name='начало рабочего дня')
    end_work_day = models.DateTimeField(verbose_name='конец рабочего дня')
    customer = models.CharField(max_length=50, verbose_name='занято')
    master = models.OneToOneField(Master)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = 'рабочее время'
        verbose_name = 'рабочее время'
