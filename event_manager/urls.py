from django.urls import path
from . import views

app_name= "event_manager"
  


urlpatterns = [
	path('home/', views.home,name='home'),
	path('category/', views.category1,name='category'),
	path('sponsers/', views.sponsers1,name='sponsers'),
	path('manage_cat/', views.manage_cat,name='manage_cat'),
	path('manage_spon/',views.manage_spon,name='manage_spon'),
	path('catdelete/<int:id>/',views.delcat,name='delcat'),
	path('add_event/', views.add_event,name='add_event'),
	path('deleve/<int:id>/',views.deleve,name='deleve'),
	path('upeve/<int:id>/',views.upeve,name='upeve'),
	path('manage_eve/',views.manage_eve,name='manage_eve'),
	path('updatecat/<int:id>/',views.updatecat,name='upcat'),
	path('delspon/<int:id>/',views.delspon,name='delspon'),
	path('updatespon/<int:id>/',views.updatespon,name='upspon'),
	path('manage_users/',views.manage_users),
	path('manage_b/',views.manage_b),
	path('admin_action/<int:id>/',views.admin_action,name='admin_action'),
	path('confirm/',views.confirm),
	path('cancel/',views.cancel),
	path('viewfeed/',views.viewfeed),
	path('addevent1/', views.addevent1,name='addevent1'),
	path('bookconf/<int:id>/',views.bookconf,name='bconf')


]