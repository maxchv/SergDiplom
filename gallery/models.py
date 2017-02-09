from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to="photos")
    title = models.CharField(blank=True, verbose_name="Заголовок", max_length=50)
    description = models.CharField(verbose_name="Краткое описание", max_length=150)
    is_nail_polish = models.BooleanField(verbose_name='Лаки', default=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Фотография работы"
        verbose_name_plural = "Фотографии работ"


class HeadImage(models.Model):
    image = models.ImageField(verbose_name="Изображение", upload_to="photos")
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.CharField(blank=True, verbose_name="Краткое описание", max_length=250,  null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение в карусели"
        verbose_name_plural = "Изображения в карусели"
