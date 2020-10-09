# Generated by Django 3.1.1 on 2020-09-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_category', '0001_initial'),
        ('eshop_products', '0005_auto_20200926_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='eshop_product_category.ProductCategory', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
