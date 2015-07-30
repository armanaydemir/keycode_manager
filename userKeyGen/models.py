from django.db import models
from django.utils import timezone
from django.http import HttpResponseRedirect
import datetime

class Customer(models.Model):
	active = models.BooleanField(default = False)
	machine_name = models.CharField(max_length=128)
	bill_amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	due_date = models.DateField(default = timezone.now() + datetime.timedelta(days=30), blank = True, null = True)	
	exchanges = models.IntegerField(default = 0)	
	invoice_date = models.DateField(default = timezone.now(), blank = True, null = True)
	keycodes_expire = models.DateField(default = timezone.now() + datetime.timedelta(days=120), blank = True, null = True)	
	name = models.CharField(max_length = 128)
	paid_date = models.DateField(default = timezone.now() + datetime.timedelta(days=30), blank = True, null = True)
	edge_hosted = 'Edge (hosted)'
	edge_nonhosted = 'Edge (non-hosted)'
	edge_risk_hosted = 'Edge Risk (hosted)'
	edge_risk_nonhosted = 'Edge Risk (non-hosted)'
	system_choices = (
		(edge_hosted, 'Edge (hosted)'),
		(edge_nonhosted, 'Edge (non-hosted)'),
		(edge_risk_hosted, 'Edge Risk (hosted)'),
		(edge_risk_nonhosted, 'Edge Risk (non-hosted)')
	)
	system = models.CharField(max_length=64, choices = system_choices, default = edge_hosted)
	
	def __unicode__(self):
        	return self.name

	def get_absolute_url(self):
		return HttpResponseRedirect('customer_detail', kwargs = {'pk': self.pk})

	def get_formatted_date(self):
		return self.keycodes_expire.strftime("%m/%d/%Y")
	
	
class User(models.Model):
	customer = models.ForeignKey('Customer')
	expiration_date = models.DateField(default = timezone.now() + datetime.timedelta(days=120))	
	name = models.CharField(max_length = 64, default = 'user')

	def __unicode__(self):
        	return self.name

	def get_formatted_date(self):
		return self.expiration_date.strftime("%m/%d/%Y")
