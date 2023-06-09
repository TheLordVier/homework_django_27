# Generated by Django 4.0.1 on 2023-04-09 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='some_slug', max_length=10, validators=[django.core.validators.MinValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=300, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
