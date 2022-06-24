# Generated by Django 4.0.5 on 2022-06-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0016_sizechoice_delete_size_choices_alter_shoes_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIZE_CHOICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Sizechoice',
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size',
            field=models.ManyToManyField(to='myapi.size_choices'),
        ),
    ]
