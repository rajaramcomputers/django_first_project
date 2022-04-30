from django.contrib import admin

# Register your models here.
from .models import staffdetails
from .models import leaveapplied

admin.site.register(staffdetails)
admin.site.register(leaveapplied)