from django.db import models
from django.contrib.auth.models import User


# custom user Profile is related to the built-in User used for auth
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=80, blank=True)
    workplace = models.CharField(max_length=80, blank=True)
    office = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=80, blank=True)
    personal_web_site = models.CharField(max_length=80, blank=True)
