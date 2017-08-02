from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import redirect,reverse

from marketplace.forms import PostForm, LoginForm, RegForm, SearchForm
from .models import User
from .models import Posts

# Create your views here.

def index(request):
	all_users = User.objects.all()
	context = {
		'all_users' : all_users,
	}
	return render(request, 'marketplace/index.html', context)
	
	
def detail(request, user_id):
	all_posts = Posts.objects.all()
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
		'form':form
	}	
	return render(request, 'marketplace/userprofile.html', context)
	
	
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
		
	return render(request,'marketplace/viewitem.html',{'posts':posts, 'loggeduser':user, 'form':form})
	
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

def makeoffer(request,post_id):

	return render(request, 'marketplace/makeoffer.html', {})