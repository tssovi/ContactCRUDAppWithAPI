# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from contactapp.models import Contact
from contactapp.serializers import ContactSerializer

class ContactMixin(object):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactList(ContactMixin, ListCreateAPIView):
    pass

class ContactDetail(ContactMixin, RetrieveUpdateDestroyAPIView):
    pass
