from django.db import models
from django.urls import reverse
from .validators import validate_file_extension

SEX_CHOICES = [
    ('Мужские', 'Мужские кроссовки'),
    ('Женские', 'Женские кроссовки'),
]

FIRM_CHOICES = [
    ('Nike', 'Nike'),
    ('Adidas', 'Adidas'),
    ('Reebok', 'Reebok'),
    ('Puma', 'Puma'),
    ('New Balance', 'New Balance'),
    ('Asics', 'Asics'),
    ('Lacoste', 'Lacoste')
]

class Size(models.Model):
    name = models.CharField('Размер',max_length=250)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField("Название категории", max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    images = models.ImageField(null=True, blank=True, upload_to='images/category/', verbose_name='Изображение')
    imageswhite = models.ImageField(null=True, blank=True, upload_to='images/category/', verbose_name='Белое изображение')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Shoes(models.Model):
    name = models.CharField('Название обуви',  max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    descriprion = models.TextField('Краткое описание товара',  max_length=5000)
    descriprion_full = models.TextField('Полное описание товара',  max_length=5000)
    sex = models.CharField(choices=SEX_CHOICES, max_length=100)
    price = models.CharField('Стоимость',  max_length=60)
    size = models.ManyToManyField(Size)
    images = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение в списке')
    images2 = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение 2')
    images3 = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение 3')
    firm = models.CharField(choices=FIRM_CHOICES, max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('open', kwargs={'shoes_slug': self.slug})

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

class Preview(models.Model):
    text = models.TextField('Текст', max_length=5000)

