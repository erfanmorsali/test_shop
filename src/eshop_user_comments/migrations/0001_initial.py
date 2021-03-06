# Generated by Django 3.1.1 on 2020-09-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=100, verbose_name='عنوان')),
                ('message', models.TextField(verbose_name='پیام شما')),
                ('is_read', models.BooleanField(default=False, verbose_name='خوانده شده / نشده')),
            ],
            options={
                'verbose_name': 'نظر کاربر',
                'verbose_name_plural': 'نظرات کاربران',
            },
        ),
    ]
