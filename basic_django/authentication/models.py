from django.db import models

from helpers.models import TrackingModel
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, UserManager)
# Create your models here.
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone


class MyUserManager(UserManager):
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

    # from django.contrib.auth.models import


class User (AbstractBaseUser, PermissionsMixin, TrackingModel):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(("username"),
                                max_length=150,
                                unique=True,
                                help_text=_(
        "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
    },
    )
    # first_name = models.CharField(_("first name"), max_length                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 =150, blank=True)
    # last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(("email address"), blank=False, unique=True)
    is_staff = models.BooleanField(("staff status"),
                                   default=False,
                                   help_text=(
        "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(("active"),
                                    default=True,
                                    help_text=(
        "Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts."
    ),
    )
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username "]
