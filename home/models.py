from django.conf import settings
from django.db import models
from django.utils import timezone


class Heropage(models.Model):
    herotitle   =   models.CharField(max_length=200)
    herotext    =   models.TextField()
    # button = models.URLField('/')

    def __str__(self):
        return self.herotitle


class Process(models.Model):
    image       =   models.ImageField(upload_to='', null=True, blank=True)
    processtext =   models.TextField()


class Gyanpage(models.Model):
    gyantitle   =   models.CharField(max_length=200)
    gyantext    =   models.TextField()
    # button = models.URLField('/')

    def __str__(self):
        return self.gyantitle


class Footerpage(models.Model):
    footertitle     =   models.CharField(max_length=200)
    footertext      =   models.TextField()

    def __str__(self):
        return self.footertitle
