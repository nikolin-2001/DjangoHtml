# Generated by Django 4.0.5 on 2022-06-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_shoes_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='images',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
