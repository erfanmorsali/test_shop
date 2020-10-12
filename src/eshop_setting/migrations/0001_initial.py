# Generated by Django 3.1.1 on 2020-09-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=50, verbose_name='ایمیل')),
                ('about_us', models.TextField(verbose_name='درباره ی ما')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='لوگو')),
            ],
        ),
    ]