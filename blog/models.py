from __future__ import unicode_literals

from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title



