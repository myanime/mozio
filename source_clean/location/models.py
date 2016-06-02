from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, default = "Donald Trump")
    email = models.CharField(max_length=100, default = "trump@whitehouse.com")
    phone_number = models.CharField(max_length=100, default = 123456)
    language = models.CharField(max_length=100, default = "spanish")
    location = models.CharField(max_length=1000, default = [1,2,3,4,5,6,7,8])
    geojson_object = models.TextField()

