from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# class CustomUser(models.Model):
#     # email = models.EmailField(blank=True, verbose_name=_('email'), unique=True)
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     birthday_year = models.PositiveIntegerField()


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, verbose_name=_('email'), unique=True)

