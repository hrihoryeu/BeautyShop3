from django.db import models
from django.urls import reverse

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, db_index=True, unique=True)
    description = models.TextField(blank=True)
    establishment = models.DateField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Type(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_index=True)
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, db_index=True)
    image = models.ImageField('Photo', upload_to='perfumes/%Y/%m/%d', blank=True)
    short_description = models.CharField(max_length=100, blank=True)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Warehouse(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
