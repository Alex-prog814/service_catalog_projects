from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', verbose_name='Категория')
    text = models.TextField(verbose_name='Содержание')
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='items', verbose_name='Изображение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('item-details', args=[str(self.id)])