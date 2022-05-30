from django.db import models
from simple_history.models import HistoricalRecords


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text = models.TextField(verbose_name='Текст статьи')
    author = models.CharField(verbose_name='Автор статьи', max_length=255)
    category = models.ManyToManyField("Category", verbose_name='Категории', related_name="category")
    tag = models.ManyToManyField("Tag", verbose_name='Теги', related_name="category")
    visible = models.BooleanField(verbose_name='Показать всем', default=False)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=255)
    description = models.TextField(verbose_name='Описание категории')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(verbose_name='Название тега', max_length=255)
    description = models.TextField(verbose_name='Описание тега')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
