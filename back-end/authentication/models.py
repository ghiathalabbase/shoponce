from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.
@deconstructible
class UnicodeUsernameValidator(RegexValidator):
    regex = r"^\w+\Z"
    message = _("Enter a valid username. This value may contain only letters, numbers, ./_ characters.")
    flags = 0

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username, email and password are required. Other fields are optional.
    """

    username_validators = [UnicodeUsernameValidator(), MinLengthValidator(6)]

    username = models.CharField(
        verbose_name=_("username"),
        max_length=60,
        unique=True,
        validators=username_validators,
        error_messages={"unique": _("This username is already taken, use another.")}
    )

    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        error_messages={"unique": _("This email is already taken, user another.")}
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    def __str__(self):
        return self.username

class User(AbstractUser):
    pass
