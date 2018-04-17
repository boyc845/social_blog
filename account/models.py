from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# account models
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200)
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='qq')
    phone_number = models.CharField(max_length=11, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-id']

    def __str__(self):
        return self.username