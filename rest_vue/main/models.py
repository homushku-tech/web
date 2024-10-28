from django.db import models

class InformationResource(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'informatinresource'
        verbose_name = 'Информационные ресурсы'
        verbose_name_plural = 'Информационные ресурсы'
        ordering = ("id",)

    def __str__(self):
        return self.name

