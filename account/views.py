from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from account import models

class UserForm(forms.Form):
	username = forms.CharField(label='UserName:',max_length=40)
	password = forms.CharField(label='PassWord:',widget=forms.PasswordInput())

# Create your views here.

def register(request):
	if request.method == "POST":
		uf = UserForm(request.POST)
		if uf.is_valid():
			#get informations from Form.
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			#write into datebase.
			user = models.UserAccount()
			user.username = username
			user.password = password
			user.save()
			return render(request,'account/success.html',{'username':username})
			#return HttpResponseRedirect(reverse('success.html',{'username':username}))
	else:
			uf = UserForm()
	return render(request,'register.html',{'uf':uf})



#	uf = UserForm(request.POST)
#	try:
#		uf.is_valid()
#	except (KeyError, UserForm.DoesNotExist):
#		return render(request, 'register.html',{
#			'error_message': "You didn't input password or name"
#			})
#	else:
#		username = uf.cleaned_data['username']
#		password = uf.cleaned_data['password']
#		user = models.User()
#		user.username = username
#		user.password = password
#		user.save()
#		return HttpResponseRedirect(reverse('success.html',{'username':username}))


		
