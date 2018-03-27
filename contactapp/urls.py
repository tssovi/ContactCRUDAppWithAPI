from django.conf.urls import url
from contactapp.views import ContactList, ContactDetail

urlpatterns = [
    url(r'^contact/$', ContactList.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>[0-9]+)$', ContactDetail.as_view(), name='contact_detail'),
]