from django.db import models
# Create your models here.



class User(models.Model):
	username = models.CharField(max_length=25)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	oChoice =(
		('Student', 'student'),
		('Staff', 'staff'),
	)
	occupation = models.CharField(
		max_length=7,
		choices=oChoice, default='student'
	)
	degree_OR_office = models.CharField(max_length=100) #degree or office
	password = models.CharField(max_length=50)
	profile_pic = models.ImageField(blank=True,upload_to='profile_image')
	regdate = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.username
	
class Posts(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	quantity = models.IntegerField(default=0)
	price = models.FloatField(default=0.0)
	dateadded = models.DateTimeField(auto_now_add=True)
	cond_choices = (
		('Brand new', 'New'),
		('Second hand', 'Used'),
		('Damaged', 'Damaged'),
	)
	condition = models.CharField(
		max_length=11,
		choices=cond_choices, default='new'
	)
	type_choices = (
		('Academic','Academics'),
		('Office', 'Office'),
	)
	type = models.CharField(
		max_length=8,
		choices=type_choices, default='acads'
	)
	course_name = models.CharField(max_length=25,blank=True)
	thumbnail = models.ImageField(blank=True,upload_to='profile_image')
	tag = models.CharField(max_length=25, blank=True)
	
	def __str__(self):
		return self.name
	