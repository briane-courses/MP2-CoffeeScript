from django import forms

from .models import User
from .models import Posts
from .models import Offer

class PostForm(forms.ModelForm):
	
    class Meta:
        model = Posts
        fields = ['name', 'quantity', 'price', 'condition', 'type', 'course_name', 'thumbnail', 'tag']
		
class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}
		
class RegForm(forms.ModelForm):
	
    class Meta:
        model = User
        fields = '__all__'
		
class SearchForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ['tag']
		
class AcceptForm(forms.ModelForm):

	class Meta:
		model = Offer
		fields = ['reason']	
		
class OfferBuyForm(forms.ModelForm):

	class Meta:
		model = Offer
		fields = ['title', 'BidAmount']
		
class OfferSwapForm(forms.ModelForm):

	class Meta:
		model = Offer
		fields = ['title', 'offer_post']	
	
	#def __init__(self,*args,**kwargs):
	#	User = kwargs.pop("user")
	#	self.fields['offer_post'].queryset = Posts.objects.filter(User = user)
	
	
	