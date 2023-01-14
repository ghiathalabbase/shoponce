from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    # email = models.EmailField(unique=True)
    # password = models.TextField()
    profile_image = models.TextField(max_length=60, null=True, default='')
    birth_date = models.DateField()
    gender = models.BooleanField()
    favourits = models.ManyToManyField('Product', related_name='favourits')
    # What's More ?

class City(models.Model):
    city = models.CharField(max_length=20)

class Category(models.Model):
    category = models.CharField(max_length=20)

class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    description = models.TextField(null=True)
    main_image = models.TextField(max_length=60, null=True, default='')
    logo = models.TextField(max_length=40, null=True, default='')
    categories = models.ManyToManyField(Category, related_name='stores')
    cities = models.ManyToManyField(City, related_name='stores')

class StoreImages(models.Model):
    picture = models.TextField(max_length=40, null=True, default='')
    related_store = models.ForeignKey(Store, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=80)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    in_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0.0)])
    main_image = models.TextField(max_length=60, null=True, default='')
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class Attributes(models.Model):
    key = models.CharField(max_length=40)
    value = models.CharField(max_length=80)
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ProductImages(models.Model):
    picture = models.TextField(max_length=40, null=True, default='')
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Discount(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    duration = models.FloatField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Tags(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, related_name='tags')