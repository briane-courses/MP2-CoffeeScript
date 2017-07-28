from django import forms

from .models import User
from .models import Posts

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