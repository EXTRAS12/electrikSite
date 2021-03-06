from django.db import models
from django.urls import reverse


class WorkList(models.Model):
    """Модель наши работы"""
    title = models.CharField(max_length=150, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class PriceCategory(models.Model):
    """Модель товаров с ценой"""
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        ordering = ['name']
