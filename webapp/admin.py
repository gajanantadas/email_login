from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','pword']
admin.site.register(User,UserAdmin)