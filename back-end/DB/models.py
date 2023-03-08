from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.deconstruct import deconstructible

from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
@deconstructible
class UnicodeUsernameValidator(RegexValidator):
    regex = r"^\w+\Z"
    message = _("Enter a valid username. This value may contain only letters, numbers, ./_ characters.")
    flags = 0

STORES_IMAGES_DIR = 'stores_images'
PRODUCTS_IMAGES_DIR = 'products_images'

class Profile(models.Model):
  name = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile_image = models.ImageField(
    upload_to='profiles_images',
    null=True,
    blank=True
  )
  favo_products = models.ManyToManyField('Product', through='FavouriteProducts')
  favo_categories = models.ManyToManyField('Category', through='FavouriteCategories')
  favo_tags = models.ManyToManyField('Tag', through='FavouriteTags')
  country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
  city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
  
  def __str__(self) -> str:
     return self.name


class Country(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class City(models.Model):
  name = models.CharField(max_length=50)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

class Category(models.Model):
  name = models.CharField(max_length=20)
  stores = models.ManyToManyField('Store', through='CategoriesStores')

  def __str__(self):
      return self.name

class FavouriteCategories(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
      return self.user.username + " | " + self.category.name

class Tag(models.Model):
  name = models.CharField(max_length=30)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null =True)
  stores = models.ManyToManyField('Store', through='TagsStores')

  def __str__(self):
      return self.name

class FavouriteTags(models.Model):
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
      return self.user.username + " | " + self.tag.name
    
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
    description = models.TextField(null=True, blank=True)
    # main_image = models.ImageField(upload_to='stores images', null=True, blank=True)
    logo = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True, blank=True)
    categories = models.ManyToManyField(Category, through='CategoriesStores')

    def __str__(self):
      return self.name

class CategoriesStores(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

  def __str__(self):
      return self.store.name + " | " + self.category.name

class TagsStores(models.Model):
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

  def __str__(self):
      return self.store.name + " | " + self.tag.name

class Branch(models.Model):
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  number = models.TextField()
  main_image = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True, blank=True)
  telegram_account = models.URLField(null=True, blank=True)
  # the rest of social media account links....
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
  is_centeral = models.BooleanField(default=False)

  def __str__(self):
      return self.store.name + " | " + self.city.name

class BranchImages(models.Model):
  picture = models.ImageField(upload_to=STORES_IMAGES_DIR, null=True,blank=True)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Product(models.Model):
  name = models.CharField(max_length=80)
  rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0)
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
  price = models.IntegerField(validators=[MinValueValidator(0.0)])
  main_image = models.ImageField(upload_to=PRODUCTS_IMAGES_DIR, null=True, blank=True)
  description = models.TextField(null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.name

# Need Discuss
class Discount(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    duration = models.FloatField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
      return self.product.name + " | " + str(self.value)

class ProductImages(models.Model):
  picture = models.ImageField(upload_to=PRODUCTS_IMAGES_DIR, null=True, blank=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

class FavouriteProducts(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)

  def __str__(self):
      return self.user.username + " | " + self.product.name