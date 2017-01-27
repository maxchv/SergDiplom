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

