from django.contrib import admin
from .models import User
from .models import Posts
from .models import Offer
# Register your models here.

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Offer)