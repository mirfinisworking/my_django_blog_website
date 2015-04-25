from django.db import models
from django.contrib import admin

# Create your models here.
class UserAccount(models.Model):
	username = models.CharField(max_length = 40)
	password = models.CharField(max_length = 20)

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')

admin.site.register(UserAccount,UserAdmin)
