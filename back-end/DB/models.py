import re
from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.deconstruct import deconstructible
from django.core import validators, mail
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
STORES_IMAGES_DIR = 'stores_images'
PRODUCTS_IMAGES_DIR = 'products_images'
# Create your models here.

@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
  regex = r"^\w+\Z"
  message = _("Enter a valid username. This value may contain only letters, numbers, ./_ characters.")
  flags = 0


class AbstractUser(AbstractBaseUser,PermissionsMixin):
  """
  An abstract base class implementing a fully featured User model with
  admin-compliant permissions.

  Username, email and password are required. Other fields are optional.
  """

  last_login = None
  username_validator = UnicodeUsernameValidator()

  username = models.CharField(
    verbose_name=_("username"),
    max_length=60,
    unique=True,
    validators=[username_validator],
    error_messages={"unique": _("This username is already token, use another one.")}
  )

  email = models.EmailField(
    verbose_name=_('email address'),
    unique=True
  )

  is_staff = models.BooleanField(
    _("staff status"),
    default=False,
    help_text=_("Designates whether the user can log into this admin site."),
  )

  objects = UserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
      verbose_name = _("user")
      verbose_name_plural = _("users")
      abstract = True
      swappable = "AUTH_USER_MODEL"

  def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

  def email_user(self, subject, message, from_email=None, **kwargs):
      """Send an email to this user."""
      mail.send_mail(subject, message, from_email, [self.email], **kwargs)
  def __str__(self):
      return self.username
  
class User(AbstractUser):
  pass

class Profile(models.Model):

  user = models.OneToOneField(User,on_delete=models.CASCADE)
  date_joined = models.DateTimeField(auto_now=True)
  last_login = models.DateTimeField(blank=True, null=True)
  profile_image = models.ImageField(
    upload_to='users_images',
    default='users_images/default_profile_img.jpg',
    null=True
  )
  favos_products = models.ManyToManyField('Product', through='FavouriteProducts')
  favos_categories = models.ManyToManyField('Categorey', through='FavouriteCategories')
  favos_tags = models.ManyToManyField('Tag', through='FavouriteTags')
  country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
  city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
  # REQUIRED_FIELDS=[]


class Country(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class City(models.Model):
  name = models.CharField(max_length=50)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

class Categorey(models.Model):
  name = models.CharField(max_length=20)
  stores = models.ManyToManyField('Store', through='CategoriesStores')

  def __str__(self):
      return self.name

class FavouriteCategories(models.Model):
  categorey = models.ForeignKey(Categorey, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

  def __str__(self):
      return self.user.username + " | " + self.categorey.name

class Tag(models.Model):
  name = models.CharField(max_length=30)
  categorey = models.ForeignKey(Categorey, on_delete=models.SET_NULL, null =True)
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
    categories = models.ManyToManyField(Categorey, through='CategoriesStores')

    def __str__(self):
      return self.name

class CategoriesStores(models.Model):
  categorey = models.ForeignKey(Categorey, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, on_delete=models.CASCADE)

  def __str__(self):
      return self.store.name + " | " + self.categorey.name

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
  category = models.ForeignKey(Categorey, on_delete=models.SET_NULL, null=True)
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