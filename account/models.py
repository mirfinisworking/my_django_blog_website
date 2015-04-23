from django.db import models

# Create your models here.
class UserAccount(models.Model):
	username = models.CharField(max_length = 40)
	password = models.CharField(max_length = 20)

class UserAdmin(models.ModelAdmin):
	list_display = ('username','password')

admin.site.register(UserAccount,UserAdmin)
