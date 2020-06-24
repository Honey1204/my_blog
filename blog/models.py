from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager,PermissionsMixin
from myblog import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s/" %(self.id)





class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name,nick_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,nick_name=nick_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name,nick_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name,nick_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email   =    models.EmailField(max_length=255,unique=True)
    name    =    models.CharField(max_length=255)
    nick_name = models.CharField(max_length=100,null=True)
    about_you = models.TextField(null=True)
    is_active   =   models.BooleanField(default=True)
    is_staff    =   models.BooleanField(default=True)

    objects =   UserProfileManager()

    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['name','nick_name']

    def __str__(self):
        return self.nick_name

    def get_full_name(self):
        return self.name

