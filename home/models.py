# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.TextField(max_length=255, null=True, blank=True)
    icon = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Drivedata(models.Model):

    #__Drivedata_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    link = models.TextField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    id = models.IntegerField(null=True, blank=True)

    #__Drivedata_FIELDS__END

    class Meta:
        verbose_name        = _("Drivedata")
        verbose_name_plural = _("Drivedata")


class Hempdata(models.Model):

    #__Hempdata_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    link = models.TextField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    ratio = models.CharField(max_length=255, null=True, blank=True)

    #__Hempdata_FIELDS__END

    class Meta:
        verbose_name        = _("Hempdata")
        verbose_name_plural = _("Hempdata")


class Boarddata(models.Model):

    #__Boarddata_FIELDS__
    link = models.TextField(max_length=255, null=True, blank=True)
    track = models.BooleanField()
    hide = models.BooleanField()

    #__Boarddata_FIELDS__END

    class Meta:
        verbose_name        = _("Boarddata")
        verbose_name_plural = _("Boarddata")


class Downloads(models.Model):

    #__Downloads_FIELDS__
    board_id = models.IntegerField(null=True, blank=True)
    filename = models.TextField(max_length=255, null=True, blank=True)

    #__Downloads_FIELDS__END

    class Meta:
        verbose_name        = _("Downloads")
        verbose_name_plural = _("Downloads")



#__MODELS__END
