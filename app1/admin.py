from django.contrib import admin
from .models import Item

from mydjango.admin import my_admin_site

# Register your models here.
#admin.site.register(Item)
my_admin_site.register(Item)
