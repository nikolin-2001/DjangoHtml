# Generated by Django 4.0.5 on 2022-06-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0017_size_choices_delete_sizechoice_alter_shoes_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Размер')),
            ],
        ),
        migrations.DeleteModel(
            name='SIZE_CHOICES',
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size',
            field=models.ManyToManyField(to='myapi.size'),
        ),
    ]
