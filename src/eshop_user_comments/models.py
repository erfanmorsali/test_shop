from django.db import models


# Create your models here.


class UserComment(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='عنوان')
    message = models.TextField(verbose_name='پیام شما')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'نظر کاربر'
        verbose_name_plural = 'نظرات کاربران'
