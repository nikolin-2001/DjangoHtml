from django.db import models

SEX_CHOICES = [
    ('Мужские', 'Мужские кроссовки'),
    ('Женские', 'Женские кроссовки'),
]

class Size(models.Model):
    name = models.CharField('Размер',max_length=250)

    def __str__(self):
        return self.name

class Shoes(models.Model):
    name = models.CharField('Название обуви',  max_length=200)
    descriprion = models.TextField('Описание',  max_length=5000)
    sex = models.CharField(choices=SEX_CHOICES, max_length=100)
    price = models.CharField('Стоимость',  max_length=60)
    size = models.ManyToManyField(Size)
    images = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return self.name


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

