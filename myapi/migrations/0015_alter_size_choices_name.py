# Generated by Django 4.0.5 on 2022-06-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0014_alter_shoes_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size_choices',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
