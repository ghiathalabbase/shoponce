from django.db import models
from django.contrib.auth.models import AbstractUser
STORES_IMAGES_DIR = 'stores images'
PRODUCTS_IMAGES_DIR = 'products images'
# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)
  #X birth_date = models.DateField()
  #X gender = models.BooleanField()
  profile_image = models.ImageField(upload_to='users images', default='users images/default profile img.jpg')
  favos_products = models.ManyToManyField('Product', through='FavouriteProducts')
  favos_categories = models.ManyToManyField('Categorey', through='FavouriteCategories')
  favos_tags = models.ManyToManyField('Tag', through='FavouriteTags')
  city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)

  # REQUIRED_FIELDS=['username']
class Country(models.Model):
  name = models.CharField(max_length=50)
class City(models.Model):
  name = models.CharField(max_length=50)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Categorey(models.Model):
  name = models.CharField(max_length=20)
  stores = models.ManyToManyField('Store', through='CategoriesStores')

class FavouriteCategories(models.Model):
  categorey = models.ForeignKey(Categorey, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
  name = models.CharField(max_length=30)
  categorey = models.ForeignKey(Categorey, on_delete=models.SET_NULL, null =True)
  stores = models.ManyToManyField('Store', through='TagsStores')

class FavouriteTags(models.Model):
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # rate = models.FloatField(min=0, max=5, default=0)
    description = models.TextField(null=True, blank=True)
    # main_image = models.ImageField(upload_to='stores images', null=True, blank=True)
    logo = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True, blank=True)
    categories = models.ManyToManyField(Categorey, through='CategoriesStores')

class CategoriesStores(models.Model):
  categorey = models.ForeignKey(Categorey, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

class TagsStores(models.Model):
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

class Branch(models.Model):
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  number = models.TextField()
  main_image = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True, blank=True)
  telegram_account = models.URLField(null=True, blank=True)
  # the rest of social media account links....
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
  is_centeral = models.BooleanField(default=False)

class BranchImages(models.Model):
  picture = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True,blank=True)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Product(models.Model):
  name = models.CharField(max_length=80)
  rate = models.FloatField()
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
  # price = models.IntegerField(min=0)
  main_image = models.ImageField(upload_to=PRODUCTS_IMAGES_DIR, null=True, blank=True)
  description = models.TextField(null=True)
  category = models.ForeignKey(Categorey, on_delete=models.SET_NULL, null=True)
  tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

class ProductImages(models.Model):
  picture = models.ImageField(upload_to=PRODUCTS_IMAGES_DIR, null=True, blank=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)



class FavouriteProducts(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  produt = models.ForeignKey(Product,on_delete=models.CASCADE)