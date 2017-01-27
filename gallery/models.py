from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name="Изображение",upload_to="photos")
    description = models.CharField(verbose_name="Краткое описание",max_length=50)

    def __str__(self):
        return self.description
