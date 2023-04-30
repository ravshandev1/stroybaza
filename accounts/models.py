from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise TypeError('Phone not')
        user = self.model(phone=phone, **extra_fields)
        user.save(using=self._db)
        user.set_password(password)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=12, unique=True, db_index=True, validators=[phone_regex])
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_birth = models.CharField(max_length=60, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = _("Telefon raqamni tasdiqlash")
        verbose_name_plural = _("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name=_("Phone number"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))

    def __str__(self):
        return self.phone


class UserCard(models.Model):
    user = models.ForeignKey(Account, models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16)
    validity_period = models.CharField(max_length=5)
    card_holder = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self
