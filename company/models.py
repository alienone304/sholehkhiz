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

    rate_cleanness = models.CharField(max_length = 264, blank = True, null =True)
    rate_beautiness = models.CharField(max_length = 264, blank = True, null =True)
    rate_clothes = models.CharField(max_length = 264, blank = True, null =True)
    rate_behaviour = models.CharField(max_length = 264, blank = True, null =True)
    rate_effectiveness = models.CharField(max_length = 264, blank = True, null =True)
    rate_overall = models.CharField(max_length = 264, blank = True, null =True)

    visiting_day = models.CharField(max_length = 264, blank = True, null =True)    


class FeedbackModel(models.Model):
    name = models.CharField(max_length = 264, blank = False, null = False)
    phone_number = models.CharField(max_length = 264, blank = True, null =True)
    address = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)

    does_visit_on_time = models.CharField(max_length = 264, blank = True, null =True)
    does_have_card = models.CharField(max_length = 264, blank = True, null =True)
    does_gave_tutorial = models.CharField(max_length = 264, blank = True, null =True)
    does_solve_problem = models.CharField(max_length = 264, blank = True, null =True)
    does_give_factor = models.CharField(max_length = 264, blank = True, null =True)
    does_announce_cost = models.CharField(max_length = 264, blank = True, null =True)
    does_gave_label = models.CharField(max_length = 264, blank = True, null =True)
    does_satisfy_you = models.CharField(max_length = 264, blank = True, null =True)

    number_of_visits = models.CharField(max_length = 264, blank = True, null =True)
