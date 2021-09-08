from django.shortcuts import render,redirect
from eventplanner.models import UserProfile
from event_manager.models import category,sponsers,Event,events,venue,decoration_theme
from .models import Booked,feedback,booking
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import random
from django.contrib import messages

from django.contrib.auth import authenticate,login

# Create your views here.


def user_event(request):
	eve=Event.objects.all()
	return render(request,"event_user.html",{'eve':eve,})

def profile(request,id):
	uppro=UserProfile.objects.get(id=id)
	if request.method=='POST':
		fn = request.POST['fname']
		ln = request.POST['lname']
		un = request.POST['uname']
		pwd = request.POST['pwd']
		em = request.POST['email']
		mob = request.POST['mob']
		addr = request.POST['address']
		up=UserProfile.objects.filter(id=id)
		up.update(mobile=mob, address=addr)
		use=User.objects.filter(id=uppro.id)
		use.update(first_name=fn, last_name=ln, username=un, password=make_password(pwd), email=em)
		return redirect('/event_user/profile/')
	return render(request,'event_user.html',{'p':uppro})

def view(request,id):
	eve=Event.objects.get(id=id)
	return render(request,"viewdet.html",{'i':eve})


def book(request,id):
	eve=Event.objects.all()
	if request.method=='POST':
		no_of_mem=request.POST['mem']
		user_re=request.POST['re']
		r=random.randint(10000,99999)
		ev=Event.objects.get(id=id)
		user=UserProfile.objects.get(user__username=request.user)	
		b=Booked(book_id=r,num_of_mem=no_of_mem,user_remark=user_re,users=user,e_name=ev)
		b.save()
		messages.success(request, "booking is sent for approval!")
		return redirect('/event_user/user_event/#team')
	return render(request,'book.html')

def my_book(request):
	book=booking.objects.filter(users__user__username=request.user)
	b=Booked.objects.filter(users__user__username=request.user)
	return render(request,"mybook.html",{'b':b,'book':book})


def updateus(request):
	user=UserProfile.objects.get(user__username=request.user)
	if request.method=='POST':
		fn = request.POST['fname']
		ln = request.POST['lname']
		un = request.POST['uname']
		pwd = request.POST['pwd']
		em = request.POST['email']
		mob = request.POST['mob']
		addr = request.POST['address']
		up=UserProfile.objects.filter(id=user.id)
		up.update(mobile=mob, address=addr)
		use=User.objects.filter(id=user.user.id)
		use.update(first_name=fn, last_name=ln, username=un, password=make_password(pwd), email=em)
		
		user = authenticate(username=un, password=pwd)
		login(request, user)
		return redirect('/event_user/user_event/')
	return render(request,'updateus.html',{'user':user})

def feedback1(request):
	user=UserProfile.objects.get(user__username=request.user)

	message = request.POST['mes']
 
	m=feedback(message=message,user=user)
	m.save()
	return redirect('/event_user/user_event/')


def cancel(request,id):
	b=Booked.objects.get(id=id)
	b.delete()
	return redirect('/event_user/my_book/')
def cancel1(request,id):
	b=booking.objects.get(id=id)
	b.delete()
	return redirect('/event_user/my_book/')


def private(request):
	eve1= events.objects.all()
	ven= venue.objects.all()
	dec= decoration_theme.objects.all()

	if request.method=="POST":
		r=random.randint(10000,99999)
		date = request.POST['date']
		per = request.POST['per']
		
		cat=request.POST['cat']
		eid=request.POST['ev']
		vid = request.POST['v']
		did= request.POST['d']
		eobj = events.objects.get(id=eid)
		vobj = venue.objects.get(id=vid)
		dobj = decoration_theme.objects.get(id=did) 
		
		uobj= UserProfile.objects.get(user__username=request.user)

		pObj= booking(book_id=r ,date=date,num_of_person=per,prices=eobj.price,ename=eobj,venue=vobj,decoration_theme=dobj,catering=cat,users=uobj)
		pObj.save()
		
		messages.success(request, "booking is sent for approval!")
		return render(request,'book1.html',{'price':eobj.price,'event':eobj.name,'pn':per,'date':date,'eid':r}) 
	return render(request, "private.html",{'ev':eve1,'ve':ven,'de':dec})


def book1(request):
	x=1
	eid=request.POST['eid']
	price=request.POST['price']
	date=request.POST['date']
	pn=request.POST['pn']
	event=request.POST['ename']
	print(eid)

	return render(request,'rec.html',{'price1':price,'event1':event,'pn1':pn,'date1':date,'eid1':eid})
	
def rec(request):
	return render(request,"rec.html")