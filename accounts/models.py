from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    
    # First Name and Last Name do not cover name patterns
    # around the globe.

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})
    is_patient = models.BooleanField(default=False)
