from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.indexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.detailView.as_view(), name='detail'),
)