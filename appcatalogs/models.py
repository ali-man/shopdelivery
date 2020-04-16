from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from imagekit.models import ImageSpecField
from mptt.models import MPTTModel, TreeForeignKey
from pilkit.processors import ResizeToFill
from pytils.translit import slugify


class Category(MPTTModel):
    parent = TreeForeignKey('self', verbose_name='Родительская категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя категории', max_length=200, unique=True)
    slug = models.SlugField(verbose_name='Slug', max_length=210, unique=True, blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/categories/%Y/%m/%d/', blank=True)
    description = RichTextUploadingField(verbose_name='Описание', blank=True)

    show = models.BooleanField(verbose_name='Вывод на сайте', default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class VolumeDesignation(models.Model):
    name = models.CharField(verbose_name='Объём', max_length=15)

    class Meta:
        verbose_name = 'Обёъм'
        verbose_name_plural = 'Объём'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Заголовок: Coca-cola 1,5л', max_length=200)
    slug = models.SlugField(verbose_name='Slug', max_length=210, unique=True, blank=True)

    price_original = models.DecimalField(verbose_name='Цена покупки', decimal_places=10, max_digits=0)
    price_own = models.DecimalField(verbose_name='Цена продажи', decimal_places=10, max_digits=0)
    price_discount = models.PositiveSmallIntegerField(verbose_name='Скидка в процентах', default=0)
    volume = models.CharField(verbose_name='Объём', default='250')
    volume_designation = models.ForeignKey(VolumeDesignation, verbose_name='Обозначение объёма', on_delete=models.PROTECT)

    action = models.BooleanField(verbose_name='Товар по акции', default=False)
    show = models.BooleanField(verbose_name='Вывод на сайте', default=True)
    created_dt = models.DateTimeField(verbose_name='Дата и время добавления товара', auto_now_add=True)
    updated_dt = models.DateTimeField(verbose_name='Дата и время обновления товара', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, **kwargs):
        super().save(**kwargs)
        if not self.slug:
            self.slug = '{}-{}'.format(self.id, slugify(self.title))

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', verbose_name='Товар', on_delete=models.CASCADE)
    file = models.ImageField(verbose_name='Изображение', upload_to='images/products/%Y/%m/%d/')
    # image_web = ImageSpecField(source='file', processors=[ResizeToFill(200, 200)],
    #                            format='JPEG', options={'quality': 90})
    # image_mob = ImageSpecField(source='file', processors=[ResizeToFill(100, 100)],
    #                            format='JPEG', options={'quality': 90})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def url(self):
        return self.file.url

    def __str__(self):
        return self.product.title


# class ProductAttribute(models.Model):
#     product = models.ForeignKey(Product, related_name='attributes', verbose_name='Товар', on_delete=models.CASCADE)
#     key = models.CharField(verbose_name='Свойтство', max_length=200)
#     value = models.CharField(verbose_name='Значание', max_length=200)
#
#     class Meta:
#         verbose_name = 'Атрибут'
#         verbose_name_plural = 'Атрибуты'
#
#     def __str__(self):
#         return '{}: {}}'.format(self.key, self.value)
