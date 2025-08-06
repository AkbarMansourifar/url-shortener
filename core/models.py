from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


#custom user manager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_field):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
#users table
class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    

#urls table
class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    created_at = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.short_url
    

#visit table
class Visit(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='visits')
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    device_type = models.CharField(max_length=10)    #mobile/desktop
    browser = models.CharField(max_length=20)


    class Meta:
        indexes = [
            models.Index(fields=['url', 'timestamp']),
        ]