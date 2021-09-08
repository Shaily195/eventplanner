from django.db import models
from eventplanner.models import UserProfile
from event_manager.models import Event,events,venue,decoration_theme

class Booked(models.Model):
	book_id =  models.IntegerField()
	num_of_mem = models.IntegerField()
	user_remark = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now=True)
	e_name = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)
	users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	status=models.IntegerField(default=0)


class booking(models.Model):
	book_id =  models.IntegerField()
	num_of_person = models.IntegerField()
	date = models.DateTimeField(auto_now=True)
	ename = models.ForeignKey(events, on_delete=models.CASCADE) 
	venue=models.ForeignKey(venue, on_delete=models.CASCADE)
	decoration_theme=models.ForeignKey(decoration_theme, on_delete=models.CASCADE)
	catering = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        )
	catering = models.CharField(choices=catering, max_length=10)
	status=models.IntegerField(default=0)
	prices= models.IntegerField()
	users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class feedback(models.Model):
	message = models.CharField(max_length=100)
	user =  models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
	date = models.DateTimeField(auto_now=True,null=True)

# Create your models here.
