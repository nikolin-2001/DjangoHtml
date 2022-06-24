# Generated by Django 4.0.5 on 2022-06-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_rename_choice_size_choices_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='size_choices',
            name='choice',
            field=models.CharField(default='', max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='size_choices',
            name='name',
            field=models.CharField(max_length=200, verbose_name='размер'),
        ),
    ]
