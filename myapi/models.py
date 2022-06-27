from django.db import models

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

class Shoes(models.Model):
    name = models.CharField('Название обуви',  max_length=200)
    descriprion = models.TextField('Описание',  max_length=5000)
    sex = models.CharField(choices=SEX_CHOICES, max_length=100)
    price = models.CharField('Стоимость',  max_length=60)
    size = models.ManyToManyField(Size)
    images = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')
    firm = models.CharField(choices=FIRM_CHOICES, max_length=100)

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

class Catalog(models.Model):
    text = models.TextField('Текст', max_length=5000)

class Preview(models.Model):
    text = models.TextField('Текст', max_length=5000)

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"