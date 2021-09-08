from django.urls import path
from . import views

app_name= "event_user"
  


urlpatterns = [
	path('user_event/', views.user_event,name='user_event'),
	path('profile/<int:id>/',views.profile,name='profile'),
	path('view/<int:id>',views.view,name='view'),
	path('book/<int:id>/',views.book,name='book'),
	path('my_book/',views.my_book),
	path('update/',views.updateus),
	path('feedback/',views.feedback1),
	path('cancel/<int:id>/',views.cancel,name='can'),
	path('private/',views.private,name='private'),
	path('book1/',views.book1),
	path('cancel1/<int:id>/',views.cancel1,name='can1'),
	path('rec/',views.rec),


]