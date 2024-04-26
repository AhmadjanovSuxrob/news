from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Yangilik(models.Model):
    sarlavha = models.CharField(max_length=25)
    matn = models.TextField()
    rasm = models.ImageField(null=True)

    class Meta:
        ordering = ('-id','-sarlavha')
    
    # Create your models here.
