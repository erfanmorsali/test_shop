from django.db import models
from eshop_product_category.models import ProductCategory
from django.contrib.auth.models import User
from django.db.models import Q
from eshop_product_tag.models import ProductTag


# Create your models here.

class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def search_product(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )

        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='عنوان در url')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    tag = models.ManyToManyField(ProductTag, blank=True, verbose_name="تگ")
    active = models.BooleanField(blank=True, null=True, verbose_name='موجود / ناموجود')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر')
    category = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    visit = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class FavouriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    class Meta:
        verbose_name = 'محصول مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'


class ProductGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    image = models.ImageField("product_gallery/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری تصویر'
        verbose_name_plural = 'گالری تصاویر'
