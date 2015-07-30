from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^customer/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='customer_detail'),
	url(r'^customer/create/$', views.CustomerCreate.as_view(), name='customer_create'),
	url(r'customer/(?P<pk>[0-9]+)/update/$', views.CustomerUpdate.as_view(), name='customer_update'),
	url(r'customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer_delete'),
	url(r'customer/(?P<pk>[0-9]+)/renewKeycodes', views.KeycodeRenewal.as_view(), name="renew_keycodes")
]
