from __future__ import unicode_literals

from django.db import models


# Stores the messages in the database
class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.CharField(max_length=140)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.email + '-' + str(self.date))

    # ensures that only 40 entries are in the database
    def check_save(self):
        objects = Contact.objects.all()
        if objects.count() == 40:
            objects[0].delete()
        self.save()
