# Generated by Django 3.1.1 on 2020-10-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0010_auto_20201003_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='product_gallery/'),
        ),
    ]
