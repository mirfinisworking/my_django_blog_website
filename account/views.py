from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
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
			user = models.User()
			user.username = username
			user.password = password
			user.save()
			return render_to_response('success.html',{'username':username})
		else:
			uf = UserForm()
		return render_to_response('register.html',{'uf':uf})
		
