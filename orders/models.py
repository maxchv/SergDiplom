from django.db import models
from django.contrib.auth.models import User


class FeedBack(models.Model):
    title  = models.CharField(max_length=100, verbose_name="Заголовок", default="")
    message = models.TextField(verbose_name="Отзыв")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации", editable=False)
    user = models.ForeignKey(User, verbose_name="Автор",editable=False)
    checked = models.BooleanField(verbose_name="Модерирован", editable=True, default=False)

    def __str__(self):
        return "Отзыв {} от {}".format(self.user.username, self.date.date())

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Master (models.Model):
    first_name = models.CharField(max_length = 100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone = models.CharField(max_length= 20, verbose_name= 'Контактный телефон')
    photo = models.ImageField(upload_to="master", verbose_name=("Фото мастера"), blank=True)
    # client = models.ForeignKey(Client)

    def __str__(self):
        return "Мастер: {} {} тел: {}".format (self.first_name, self.last_name, self.phone)

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Order(models.Model):
    client = models.ForeignKey(User, verbose_name="Клиент")
    datetime = models.DateTimeField(verbose_name="Время")
    canceled = models.BooleanField(verbose_name="Отменен", default=False)
    phone = models.CharField(max_length=20,verbose_name="Контактный телефон")
    master = models.ForeignKey(Master, verbose_name='Мастер')
    timestamp = models.DateTimeField(verbose_name="Время заказа", auto_now_add=True)

    def __str__(self):
        return "Заказ № {} от {}".format(self.id, self.timestamp)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"