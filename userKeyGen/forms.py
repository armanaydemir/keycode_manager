from django.forms import ModelForm
from .models import Customer, User

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['name', 'machine_name', 'system', 'bill_amount', 'exchanges', 'due_date', 'invoice_date', 'keycodes_expire', 'paid_date', 'active']

class KeycodeRenewalForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['keycodes_expire']
