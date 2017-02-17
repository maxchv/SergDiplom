from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# FIXME: не используется. На будующее
class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    class Meta:
        verbose_name = 'Профиль клиента'
        verbose_name_plural = 'Профили клиентов'

    def __str__(self):
        return self.user.username


class Master(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО мастера')
    contact_phone = models.CharField(max_length=20, verbose_name='Контактный телефон')
    master_photo = models.ImageField(blank=True, upload_to="master", verbose_name="Фото мастера")

    def __str__(self):
        return "Мастер:  {};  тел: {}".format(self.full_name, self.contact_phone)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


# FIXME: Не использутеся. На будующее
class Work_Time(models.Model):
    start_work_day = models.DateTimeField(verbose_name='начало рабочего дня')
    end_work_day = models.DateTimeField(verbose_name='конец рабочего дня')
    customer = models.CharField(max_length=50, verbose_name='занято')
    master = models.OneToOneField(Master)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = 'Рабочее время'
        verbose_name = 'Рабочее время'


class Address(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.CharField(max_length=100, verbose_name='Здание/дом')
    additional = models.CharField(blank=True, max_length=200, verbose_name='Дополнительая информация')
    office = models.CharField(max_length=250, verbose_name='Офис')
    phone = models.CharField(max_length=25, verbose_name='Телефон', unique=True)
    map_latitude = models.FloatField(blank=True, help_text='Для карты', null=True, verbose_name='Широта')
    map_longitude = models.FloatField(blank=True, help_text='Для карты', null=True, verbose_name='Долгота')
    vk = models.CharField(blank=True, max_length=250, null=True, verbose_name="VK")
    instagram = models.CharField(blank=True, null=True, max_length=250, verbose_name="Instagram")

    def __str__(self):
        return self.office

    class Meta:
        verbose_name_plural = 'Адреса'
        verbose_name = 'Адрес'


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение', upload_to='section')
    content = models.TextField(verbose_name='Содержимое раздела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Разделы'
        verbose_name = 'Раздел'
