from django.db import models
from email.mime import image
from django.db import models


# Create your models here.
class image(models.Model):

    name = models.Charfield(max_length= 35)
    description = models.Charfield(max_length = 200)


class category(models.Model):
    name = models.Charfield(max_length = 35)


class location(models.Model):
    name = models. Charfield(max_length = 35)