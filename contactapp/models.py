# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return '%s %s %s %s' % (self.name, self.address, self.phone_no, self.email)

class Meta:
    db_table = 'contactapp_contact'
