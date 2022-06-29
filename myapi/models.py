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
    descriprion = models.TextField('Описание',  max_length=5000)
    sex = models.CharField(choices=SEX_CHOICES, max_length=100)
    price = models.CharField('Стоимость',  max_length=60)
    size = models.ManyToManyField(Size)
    images = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')
    firm = models.CharField(choices=FIRM_CHOICES, max_length=100)
    cat = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('open', kwargs={'shoes_id': self.pk})

    class Meta:
        verbose_name = 'обувь'
        verbose_name_plural = 'обувь'



class Jeans(models.Model):
    name = models.CharField('Название джинс', max_length=200)
    descriprion = models.TextField('Описание', max_length=5000)
    price = models.CharField('Стоимость', max_length=50)
    class Meta:
        verbose_name = 'джинсы'
        verbose_name_plural = 'джинсы'

class Tshirt(models.Model):
    name = models.CharField('Название футболки', max_length=200)
    descriprion = models.TextField('Описание', max_length=5000)
    price = models.CharField('Стоимость', max_length=50)
    class Meta:
        verbose_name = 'футболку'
        verbose_name_plural = 'футболки'

class Sweatshirts(models.Model):
    name = models.CharField('Название кофты', max_length=200)
    descriprion = models.TextField('Описание', max_length=5000)
    price = models.CharField('Стоимость', max_length=50)
    class Meta:
        verbose_name = 'кофту'
        verbose_name_plural = 'кофты'

class Catalog(models.Model):
    text = models.TextField('Текст', max_length=5000)

class Preview(models.Model):
    text = models.TextField('Текст', max_length=5000)

