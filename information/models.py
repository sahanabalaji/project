from __future__ import unicode_literals

from django.db import models


class information(models.Model):
    name=models.CharField(max_length=255, default=None)
    location=models.CharField(max_length=255, default=None)
    hotel_code=models.CharField(max_length=255, default=None)

    def __unicode__(self):return self.name
