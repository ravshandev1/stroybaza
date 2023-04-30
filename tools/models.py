from django.db import models
from accounts.models import Account
from django.conf import settings


class Location(models.Model):
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    address_name = models.CharField(max_length=222, null=True, blank=True)
    house = models.CharField(max_length=23, null=True, blank=True)
    flat = models.CharField(max_length=23, null=True, blank=True)
    floor = models.CharField(max_length=23, null=True, blank=True)
    comment = models.CharField(max_length=333, null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.address_name


class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')
    name = models.CharField(max_length=444)

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"
