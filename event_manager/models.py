

# Create your models here.
from django.db import models
from eventplanner.models import UserProfile

# Create your models here.
class category(models.Model):
	catname = models.CharField(max_length=50,unique=True)
	desc = models.CharField(max_length=200,null=True)
	dated = models.DateTimeField(auto_now=True,null=True)

class sponsers(models.Model):
	sponser = models.CharField(max_length=50,unique=True)
	logo = models.ImageField(upload_to="product_image", blank=True)


class Event(models.Model):
	name = models.CharField(max_length=100,null=True)
	desc = models.CharField(max_length=200,null=True)
	eve_img = models.ImageField(upload_to="product_image", blank=True,null=True)
	category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
	sponsers= models.ForeignKey(sponsers,on_delete=models.CASCADE,null=True)
	location= models.CharField(max_length=50,null=True)
	startdate= models.DateField(null=True)
	enddate= models.DateField(null=True)
	speaker_name=models.CharField(max_length=100,null=True)
	added_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)

	
class manage_book(models.Model):
	admin_remark=models.CharField(max_length=50,null=True)
	choice=( 
		('confirm', 'confirm'),
        ('cancel', 'cancel'),
        )
	action = models.CharField(choices=choice, max_length=10,null=True)

class venue(models.Model):
	ven=models.CharField(max_length=50)

class decoration_theme(models.Model):
	dec=models.CharField(max_length=50)

class events(models.Model):
	name = models.CharField(max_length=100)
	eve_img = models.ImageField(upload_to="product_image")
	price= models.DecimalField(decimal_places=2, max_digits=12)
	added_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)

    
	
# Create your models here.
