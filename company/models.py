from django.db import models
from django.utils import timezone

class ContactUsModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    phone_number = models.CharField(max_length = 264, blank = True, null =True)
    request = models.TextField(null = True, blank = True)
    contacted_at = models.DateTimeField(default=timezone.now)


class ComplaintModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    phone_number = models.CharField(max_length = 264, blank = False, null =False)
    request = models.TextField(null = False, blank = False)
    picture = models.ImageField(null = True, blank = True, upload_to=r'complaint/',default = r'cataloges/default/default.jpeg')
    complained_at = models.DateTimeField(default=timezone.now)
