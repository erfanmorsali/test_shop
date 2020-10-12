# Generated by Django 3.1.1 on 2020-09-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(null=True, upload_to='sliders/', verbose_name='تصویر')),
                ('link', models.URLField(verbose_name='لینک')),
            ],
        ),
    ]