from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=223)
    category = models.ForeignKey(Category, models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Color(models.Model):
    COLORS = (
        ('FF0000', 'Red'),
        ('00FFFF', 'Cyan'),
        ('0000FF', 'Blue'),
        ('800080', 'Purple'),
        ('FFFF00', 'Yellow'),
        ('FFFFFF', 'White'),
        ('000000', 'Black'),
        ('008000', 'Green'),
        ('C0C0C0', 'Silver'),
        ('FF00FF', 'Magenta'),
        ('FFA500', 'Orange'),
        ('800000', 'Maroon'),
        ('808000', 'Olive'),
    )
    name = models.CharField(max_length=6, choices=COLORS)

    def __str__(self):
        return self.get_name_display()


class Market(models.Model):
    name = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/')
    rate = models.IntegerField(default=1)
    delivery_price = models.PositiveIntegerField(default=0)
    work_time = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=223)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, models.SET('Brand deleted'), related_name='products')
    price = models.PositiveIntegerField()
    colors = models.ManyToManyField(Color)
    description = models.TextField()
    characteristic = models.TextField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_image/')

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"
