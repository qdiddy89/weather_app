from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Location(models.Model):
    uname = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.zip_code
