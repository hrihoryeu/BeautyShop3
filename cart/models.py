from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.


class OrderDetail(models.Model):
    user = models.CharField(max_length=30, unique=True, null=True, default='')
    json = models.JSONField(null=True)

    def __str__(self):
        return self.user

