from django.db import models

class Shoes(models.Model):
    name = models.CharField('Название обуви', max_length=200)
    descriprion = models.TextField('Описание', max_length=5000)
    price = models.CharField('Стоимость', max_length=50)

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

