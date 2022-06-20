from django.contrib import admin
from .models import userSignup

# Register your models here.

class usersignupAdmin(admin.ModelAdmin):
    list_display=["firstname","lastname","username","city","state","mobile"]

admin.site.register(userSignup,usersignupAdmin)