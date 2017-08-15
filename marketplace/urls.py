from django.conf.urls import url
from . import views

app_name = 'marketplace'

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
	url(r'^makeoffer/([0-9]+)/$',views.makeoffer, name='makeoffer'),
	url(r'^filtersCond/([0-9]+)/$',views.filtersCond, name='filtersC'),
	url(r'^filtersType/([0-9]+)/$',views.filtersType, name='filtersT'),
	url(r'^filtersCourse/([0-9]+)/$',views.filtersCourse, name='filtersCo'),
	url(r'^search/([0-9]+)/$',views.filtersTag, name='filtersTa'),
	url(r'^profile/([0-9]+)/([0-9]+)/$', views.detail2, name='popup'),
	url(r'^viewitem/([0-9]+)/([0-9]+)/$', views.itemdetails2, name='popup2'),
	url(r'^accept/([0-9]+)/([0-9]+)/$', views.accept, name='accept'),
	url(r'^decline/([0-9]+)/([0-9]+)/$', views.decline, name='decline'),
	url(r'^update/([0-9]+)/$', views.updateoffer, name='update'),

]