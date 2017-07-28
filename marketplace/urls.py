from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^$',views.index, name='index'),
	
	#url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
	
	#add here /profile and other shit
	url(r'^profile/([0-9]+)/$', views.detail, name='profile'),
	url(r'^profile/$', views.index, name='trial'),
	url(r'^home/$',views.home, name='home' ),
	url(r'^login/$',views.loginNow, name='login' ),
	url(r'^addpost/$',views.addpost, name='addpost'),
	url(r'^logout/$',views.logoutNow, name='logout'),
	url(r'^signup/$',views.create_user, name='signup'),
	url(r'^viewitem/([0-9]+)/$',views.itemdetails,name='itemdetails'),
	url(r'^search/$',views.search, name='search'),
]