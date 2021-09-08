
from django.shortcuts import render,redirect
from .models import category,Event,sponsers,manage_book,events
from eventplanner.models import UserProfile
import datetime
from django.contrib import messages
from event_user.models import Booked,feedback,booking
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.
def home(request):
	return render(request, "event_manager.html")

def category1(request):
	if request.method=="POST":
		cat = request.POST['name']
		desc = request.POST['desc']
		cobj = category(catname=cat,desc= desc)
		cobj.save()
		messages.success(request, "category added Successfully!")
		return redirect('/event_manager/category/')
	return render(request, "addcategory.html")

def sponsers1(request):
	if request.method=="POST":
		sponser = request.POST['sponser']
		logo = request.FILES['img']
		s= sponsers(sponser=sponser,logo=logo)
		s.save()
		return redirect('/event_manager/sponsers')
	return render(request, "addsponsers.html")



def add_event(request):
	cobjs= category.objects.all()
	spons= sponsers.objects.all()


	if request.method=="POST":
		nm = request.POST['name']
		desc = request.POST['desc']
		img = request.FILES['img']
		start_date= request.POST['sdate']
		end_date= request.POST['edate']
		location= request.POST['location']
		speaker = request.POST['sp']
		catid = request.POST['cat']
		sid= request.POST['s']
		cobj = category.objects.get(id=catid)
		spon = sponsers.objects.get(id=sid)
		
		uobj= UserProfile.objects.get(user__username=request.user)

		pObj= Event(name=nm ,desc=desc, eve_img=img, category=cobj, added_by=uobj,sponsers=spon,startdate=start_date,enddate=end_date,location=location,speaker_name=speaker)
		pObj.save()
		messages.success(request, "Event added Successfully!")
		return redirect('/event_manager/add_event/')

	return render(request, "addevent.html",{'cats':cobjs,'s':spons})

def manage_eve(request):
	eve=Event.objects.all()
	return render(request,"manageeve.html",{'eve':eve})

def deleve(request,id):
	deleve=Event.objects.get(id=id)
	deleve.delete()
	return redirect('/event_manager/manage_eve/')

def upeve(request,id):
	cobjs= category.objects.all()
	upeve=Event.objects.get(id=id)
	spons= sponsers.objects.all()
	if request.method=='POST':
		nm=request.POST['name']
		desc=request.POST['desc']
		location= request.POST['location']
		start_date=request.POST['sdate']
		end_date=request.POST['edate']
		catid = request.POST['cat']
		sid=request.POST['s']
		spon = sponsers.objects.get(id=sid)
		cobj = category.objects.get(id=catid)
		uobj= UserProfile.objects.get(user__username=request.user)
		up=Event.objects.filter(id=id)
		up.update(name=nm ,desc=desc,startdate=start_date,enddate=end_date, category=cobj,sponsers=spon,location=location, added_by=uobj)
		return redirect('/event_manager/manage_eve/')
	return render(request,'updateeve.html',{'eve':upeve,'cats':cobjs,'s':spons})


def manage_cat(request):
	cat=category.objects.all()

	return render(request, "managecat.html",{'cat':cat})

def manage_spon(request):
	spon=sponsers.objects.all()
	return render(request,"managespon.html",{'spon':spon})

   

def delcat(request,id):
	delcate=category.objects.get(id=id)
	delcate.delete()
	return redirect('/event_manager/manage_cat/')

def delspon(request,id):
	delspon=sponsers.objects.get(id=id)
	delspon.delete()
	return redirect('/event_manager/manage_spon/')


def updatecat(request,id):
	upcat=category.objects.get(id=id)
	if request.method=='POST':
		name=request.POST['name']
		desc=request.POST['desc']
		up=category.objects.filter(id=id)
		up.update(catname=name,desc=desc)
		return redirect('/event_manager/manage_cat/')
	return render(request,'catupdate.html',{'cat':upcat})

def updatespon(request,id):
	upspon=sponsers.objects.get(id=id)
	if request.method=='POST':
		name=request.POST['name']
		logo=request.POST['img']
		spon=sponsers.objects.filter(id=id)
		spon.update(sponser=name,logo=logo)
		return redirect('/event_manager/manage_spon/')
	return render(request,'sponupdate.html',{'spon':upspon})

def manage_users(request):
	
	user=UserProfile.objects.filter(usertype='event_user')
	
	return render(request,'manageuser.html',{"user":user})

def manage_b(request):
	bk=booking.objects.all()
	book=Booked.objects.all()
	return render(request,'allbook.html',{'book':book,'bk':bk})

def bookconf(request,id):
	book=booking.objects.filter(id=id)
	book.update(status=1)
	if request.method=='POST':
		remark=request.POST['remark']
		action= request.POST['action']
		if action=='confirm':
			b=booking.objects.get(id=id)
			email=b.users.user.email
			subject = 'Thank you'
			message = 'Your event is confirmed'
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [email,]
			send_mail( subject, message, email_from, recipient_list )
		b=manage_book(admin_remark=remark,action=action)
		b.save()
		return redirect('/event_manager/manage_b/')
	return render(request,'admin_action.html')
	

def admin_action(request,id):
    book=Booked.objects.filter(id=id)
    if request.method=='POST':
    	remark=request.POST['remark']
    	action= request.POST['action']
    	if action=='confirm':
    		book.update(status=1)
    		b=Booked.objects.get(id=id)
    		email=b.users.user.email
    		subject = 'Thank you'
    		message = 'Your event is confirmed'
    		email_from = settings.EMAIL_HOST_USER
    		recipient_list = [email,]
    		send_mail( subject, message, email_from, recipient_list )
    	b=manage_book(admin_remark=remark,action=action)
    	b.save()
    	return redirect('/event_manager/manage_b/')
    return render(request,'admin_action.html')


def confirm(request):
	book=Booked.objects.filter(status=1)
	b = booking.objects.filter(status=1)
	return render(request,'confirm.html',{'book':book,'b':b})
	
def cancel(request): 
	book=Booked.objects.filter(status=0)
	b = booking.objects.filter(status=0)
	return render(request,'cancel.html',{'book':book,'b':b})
	
def viewfeed(request):
	f=feedback.objects.all()
	return render(request,'feed.html',{'f':f})

def addevent1(request):
	if request.method=='POST':
		nm=request.POST['name']
		img = request.FILES['img']
		price= request.POST['price']
		uobj= UserProfile.objects.get(user__username=request.user)

		pObj= events(name=nm , eve_img=img,price=price,added_by=uobj)
		pObj.save()
		messages.success(request, "Event added Successfully!")
		return redirect('/event_manager/addevent1/')
	return render(request, "addevent1.html")


