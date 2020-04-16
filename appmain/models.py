from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.flatpages.models import FlatPage
from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class ProjectConfig(SingletonModel):
    name = models.CharField(verbose_name='Название проекта', default='TezFood')
    logo = models.ImageField(verbose_name='Логотип проекта', upload_to='images/project/')
    phone = models.CharField(verbose_name='Телефон поддержки', default='+998914266874')
    time_work = RichTextUploadingField(verbose_name='Режим работы', blank=True)
    currency = models.CharField(verbose_name='Валюта', default='сум')
    quantity_products_page = models.PositiveSmallIntegerField(verbose_name='Количество товаров на странице', default=20)
    footer_text = models.TextField(verbose_name='Текст в подвале сайта',
                                   default='Created by <a href="https://t.me/alimanuz" target="_blank" >Ali-man</a>')
    verbose_name = 'Настройка проекта'
    verbose_name_plural = 'Настроки проекта'

    def __str__(self):
        return self.verbose_name


class NewFlatPage(models.Model):
    flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    description = RichTextUploadingField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.flatpage.title


class Feedback(models.Model):
    STATUS = (
        (0, 'В ожидании'),
        (1, 'На рассмотрении'),
        (2, 'Выполнено'),
    )

    name = models.CharField(verbose_name='Имя', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=100, blank=True)
    message = models.TextField(verbose_name='Сообщение')

    status = models.SmallIntegerField(verbose_name='Статус', max_length=100, choices=STATUS, default=0)
    created_datetime = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.name
