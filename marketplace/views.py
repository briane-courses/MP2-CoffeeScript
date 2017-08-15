from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import redirect,reverse
from django.urls import reverse

from marketplace.forms import PostForm, LoginForm, RegForm, SearchForm, OfferBuyForm, OfferSwapForm,AcceptForm
from .models import User
from .models import Posts
from .models import Offer

# Create your views here.

def index(request):
	all_users = User.objects.all()
	context = {
		'all_users' : all_users,
	}
	return render(request, 'marketplace/index.html', context)
	
	
def detail(request, user_id):
	all_posts = Posts.objects.all()
	all_offers = Offer.objects.all()
	try:
		user = User.objects.get(pk=user_id)
	except (KeyError, User.DoesNotExist):
		raise Http404("User does not exist")
	
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form})
	
	context = {
		'user': user,
		'loggeduser':loggeduser,
		'form':form,
		'all_offers':all_offers,
		'all_posts':all_posts,
	}	
	return render(request, 'marketplace/userprofile.html', context)
	
def detail2(request, user_id,offer_id):
	all_posts = Posts.objects.all()
	all_offers = Offer.objects.all()
	try:
		user = User.objects.get(pk=user_id)
	except (KeyError, User.DoesNotExist):
		raise Http404("User does not exist")
		
	offer = Offer.objects.get(pk=offer_id)
	
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form})
	
	context = {
		'user': user,
		'loggeduser':loggeduser,
		'form':form,
		'all_offers':all_offers,
		'all_posts':all_posts,
		'offer':offer,
	}	
	return render(request, 'marketplace/userprofile2.html', context)
	
def home(request):
	
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = 0
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	if query != '':
		all_posts = Posts.objects.all()
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form})
	
	filter_number = 10
	if request.POST:
		post_num = request.POST.get("numberz",False)
		filter_number = int(post_num)
		print(filter_number)
		print(type(filter_number))
		
	if request.POST.get("more"):
		filter_number = filter_number + 5
		
	all_posts = Posts.objects.all().order_by('?')[:filter_number]
	
	
	context = {
		'all_posts': all_posts,
		'loggeduser':loggeduser,
		'form':form,	
	}
	return render(request, 'marketplace/home.html', context)
	
def addpost(request):
	form = PostForm(request.POST or None, request.FILES or None)
	user_id = request.session['USERZ']
	user = User.objects.get(pk=user_id)
	all_posts = Posts.objects.all()
	if form.is_valid():
		post = form.save(commit=False)
		post.user = user
		post.save()
		return render(request, 'marketplace/home.html', {'all_posts': all_posts,'loggeduser':user})
	
	form2 = SearchForm(request.POST)
	queryTag = form2.save(commit=False)
	query = form2.cleaned_data["tag"]
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':user, 'form':form2})
	return render(request, 'marketplace/addpost.html', {'form':form, 'loggeduser':user,'form2':form2})	
	
def loginNow(request):
	form = LoginForm(request.POST)
	all_users = User.objects.all()
	all_posts = Posts.objects.all()
	if form.is_valid():
		LPass =	form.cleaned_data["password"]
		LUser = form.cleaned_data["username"]
		for i in all_users:
			if i.username == LUser:
				if i.password == LPass:
					print ('LOGGED IN')
					request.session['USERZ'] = i.id
					form2 = SearchForm(request.POST)
					queryTag = form2.save(commit=False)
					query = form2.cleaned_data["tag"]
					if query != '':
						return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form2})
					return render(request, 'marketplace/home.html', {'loggeduser': i, 'all_posts':all_posts, 'form':form2})
				else:
					print ('WRONG PASS')
			else:
				print ('Account not found')
				
	return render(request, 'marketplace/login.html', {'form':form})

def logoutNow(request):
	del request.session['USERZ']
	all_posts = Posts.objects.all()
	loggeduser = None
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form})
	
	render(request, 'marketplace/logout.html')
	return render(request, 'marketplace/home.html',{'all_posts':all_posts,'form':form})

def create_user(request):
	form = RegForm(request.POST or None, request.FILES or None)
	all_posts = Posts.objects.all()
	if form.is_valid():
		user = form.save(commit=False)
		user.save()
		return render(request, 'marketplace/home.html', {'all_posts':all_posts} )
	
	return render(request, 'marketplace/signup.html', {'form':form})

def itemdetails(request,post_id):
	all_posts = Posts.objects.all()
	all_offers = Offer.objects.all()
	posts = Posts.objects.get(pk=post_id)
	try:
		user = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		user = None
	
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':user, 'form':form})
		
	return render(request,'marketplace/viewitem.html',{'posts':posts, 'loggeduser':user, 'form':form,'all_offers':all_offers})

def itemdetails2(request,post_id,offer_id):
	all_posts = Posts.objects.all()
	all_offers = Offer.objects.all()
	posts = Posts.objects.get(pk=post_id)
	offer = Offer.objects.get(pk=offer_id)
	off_type = offer.OfferType
	checker = 0
	
	try:
		user = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		user = None
	
	form = SearchForm(request.POST)
	queryTag = form.save(commit=False)
	query = form.cleaned_data["tag"]
	
	if request.POST.get("Update"):
		checker = 1
		
		if off_type == 'Buy':
			form = OfferBuyForm(request.POST or None, request.FILES or None)
		elif off_type == 'Swap':
			form = OfferSwapForm(request.POST or None, request.FILES or None)
			form.fields['offer_post'].queryset = Posts.objects.filter(user = user)
		
		if form.is_valid():
			offer = form.save(commit=False)
			offer.save();
			return render(request,'marketplace/viewitem2.html',{'all_posts':all_posts,'posts':posts, 'loggeduser':user, 'form':form,'all_offers':all_offers,'offer':offer})
	
	if request.POST.get("Cancel"):
		offer.delete()	
		return render(request,'marketplace/home.html',{'all_posts':all_posts, 'loggeduser':user, 'form':form,'all_offers':all_offers})
	
	if query != '':
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':user, 'form':form})
		
	return render(request,'marketplace/viewitem2.html',{'all_posts':all_posts,'posts':posts, 'loggeduser':user, 'form':form,'all_offers':all_offers,'offer':offer})
	
def search(request):
	form = SearchForm(request.POST)
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
	all_posts = Posts.objects.all()
	if form.is_valid():
		queryTag = form.save(commit=False)
		query = form.cleaned_data["tag"]
		return render(request, 'marketplace/search.html', {'all_posts':all_posts, 'query':query,'loggeduser':loggeduser, 'form':form})
				
	
	return render(request, 'marketplace/search.html', {'loggeduser':loggeduser,'form':form})

def filtersCond(request,post_id):
	form = SearchForm(request.POST)
	all_posts = Posts.objects.all()
	choice = Posts.objects.get(pk=post_id)
	query = choice.condition

	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
		
	return render(request, 'marketplace/filters.html', {'query':query, 'all_posts':all_posts,'loggeduser':loggeduser,'form':form})
	
def filtersType(request,post_id):
	form = SearchForm(request.POST)
	all_posts = Posts.objects.all()
	choice = Posts.objects.get(pk=post_id)
	query = choice.type

	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
		
	return render(request, 'marketplace/filters.html', {'query':query, 'all_posts':all_posts,'loggeduser':loggeduser,'form':form})

def filtersCourse(request,post_id):
	form = SearchForm(request.POST)
	all_posts = Posts.objects.all()
	choice = Posts.objects.get(pk=post_id)
	query = choice.course_name

	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
		
	return render(request, 'marketplace/filters.html', {'query':query, 'all_posts':all_posts,'loggeduser':loggeduser,'form':form})

def filtersTag(request,post_id):
	form = SearchForm(request.POST)
	all_posts = Posts.objects.all()
	choice = Posts.objects.get(pk=post_id)
	query = choice.tag

	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
		
	return render(request, 'marketplace/search.html', {'query':query, 'all_posts':all_posts,'loggeduser':loggeduser,'form':form})

def accept(request,userid,offer_id):
	form = AcceptForm(request.POST)
	form2 = SearchForm(request.POST)
	offerz = Offer.objects.get(pk=offer_id)
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
	
	all_posts = Posts.objects.all()
	
	if request.method == 'POST':
		if form.is_valid():
			reason = form.save(commit=False)
			reasonQ = form.cleaned_data["reason"]
			offerz.reason = reasonQ
			offerz.OfferStat = 'Accept'
			offerz.save()
			return render(request, 'marketplace/home.html',{'loggeduser':loggeduser,'form':form2,'all_posts':all_posts})
				
	return render(request, 'marketplace/accept.html', {'loggeduser':loggeduser,'form':form})

def decline(request,userid,offer_id):
	form = AcceptForm(request.POST)
	form2 = SearchForm(request.POST)
	offerz = Offer.objects.get(pk=offer_id)
	try:
		loggeduser = User.objects.get(id=request.session['USERZ'])
	except (KeyError, User.DoesNotExist):
		loggeduser = None
	
	all_posts = Posts.objects.all()
	
	if request.method == 'POST':
		if form.is_valid():
			reason = form.save(commit=False)
			reasonQ = form.cleaned_data["reason"]
			offerz.reason = reasonQ
			offerz.OfferStat = 'Decline'
			offerz.save()
			return render(request, 'marketplace/home.html',{'loggeduser':loggeduser,'form':form2,'all_posts':all_posts})
				
	return render(request, 'marketplace/accept.html', {'loggeduser':loggeduser,'form':form})
	
def makeoffer(request,post_id):
	all_posts = Posts.objects.all()
	user_id = request.session['USERZ']
	user = User.objects.get(pk=user_id)
	off_type = 'Swap'
	pozt = Posts.objects.get(pk=post_id)
	form = OfferSwapForm(request.POST or None, request.FILES or None)
	
	if request.POST.get("offertype"):
		off_type = request.POST.get("offertype", False)
	
	if off_type == 'Buy':
		form = OfferBuyForm(request.POST or None, request.FILES or None)
	elif off_type == 'Swap':
		form = OfferSwapForm(request.POST or None, request.FILES or None)
		#form.offer_post.queryset = Posts.objects.filter(user_id = user_id)
	
	if form.is_valid():
		offer = form.save(commit=False)
		offer.post_To = pozt
		offer.user_Offer = user
		offer.OfferType = off_type
		if off_type == 'Buy':
			offer.offer_post = null
		
		offer.save();
		return render(request, 'marketplace/home.html', {'all_posts': all_posts,'loggeduser':user})
		
	return render(request, 'marketplace/makeoffer.html', {'form':form, 'loggeduser':user})

def updateoffer(request,offer_id):
	all_posts = Posts.objects.all()
	user_id = request.session['USERZ']
	user = User.objects.get(pk=user_id)
	offer = Offer.objects.get(pk=offer_id)
	off_type = 'Swap'
	form = OfferSwapForm(request.POST or None, request.FILES or None)
	
	if request.POST.get("offertype"):
		off_type = request.POST.get("offertype", False)
	
	if off_type == 'Buy':
		form = OfferBuyForm(request.POST or None, request.FILES or None)
	elif off_type == 'Swap':
		form = OfferSwapForm(request.POST or None, request.FILES or None)
		form.fields['offer_post'].queryset = Posts.objects.filter(user = user)
	
	if form.is_valid():
		offer = form.save(commit=False)
		offer.OfferType = off_type		
		offer.save();
		return render(request, 'marketplace/home.html', {'all_posts': all_posts,'loggeduser':user})
		
	return render(request, 'marketplace/update.html', {'form':form, 'loggeduser':user})	
	