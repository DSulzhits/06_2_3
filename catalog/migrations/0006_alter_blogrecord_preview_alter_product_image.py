# Generated by Django 4.2.1 on 2023-06-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_blogrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecord',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='images/records/', verbose_name='изображение(превью)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='изображение(превью)'),
        ),
    ]
