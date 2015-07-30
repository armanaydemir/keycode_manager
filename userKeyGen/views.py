from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from .forms import CustomerForm, KeycodeRenewalForm
from .models import Customer, User
from django.forms.models import inlineformset_factory
from django.contrib import messages
import subprocess
import paramiko
import time

class IndexView(generic.ListView):
	model = Customer
	context_object_name = 'customerList'
	
	def get_queryset(self):
		return Customer.objects.order_by('name')[:]

class DetailView(generic.DetailView):
	model = Customer
	template_name = 'userKeyGen/customer_detail.html'

class CustomerCreate(generic.CreateView):
	model = Customer
	form_class = CustomerForm
	userCreateFormSet = inlineformset_factory(Customer, User, fields=['name', 'expiration_date'], extra=1, can_delete=True)
	
	def form_valid(self, form, inlines):
		if inlines.is_valid() and form.is_valid():
			inlines.save()
			form.save()
			return HttpResponseRedirect('/userKeyGen/customer/'+str(self.object.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

	def form_invalid(self, form, inlines):
		return self.render_to_response(self.get_context_data(form=form, inlines=inlines))

	def get_context_data(self, **kwargs):
		ctx = super(CustomerCreate, self).get_context_data(**kwargs)
		if self.request.POST:
			ctx['form'] = CustomerForm(self.request.POST)
			ctx['inlines'] = self.userCreateFormSet(self.request.POST)
			ctx['message'] = messages.add_message(self.request, messages.SUCCESS, 'SUCCESS: Customer created')
		else:
			ctx['form'] = CustomerForm()
			ctx['inlines'] = self.userCreateFormSet()
			ctx['message'] = messages.add_message(self.request, messages.ERROR, 'ERROR: Customer not created')
		return ctx

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, instance=self.object)
		inlines = self.userFormSet(request.POST, request.FILES, instance=self.object)
		if form.is_valid() and inlines.is_valid():
			return self.form_valid(form, inlines)
		else:
			return self.form_invalid(form, inlines)

class CustomerUpdate(generic.UpdateView):
	model = Customer
	form_class = CustomerForm
	template_name_suffix = '_update_form'
	userFormSet = inlineformset_factory(Customer, User, fields=['expiration_date'], extra=0)

	def get_context_data(self, **kwargs):		
		userList = self.userFormSet(queryset = self.object.user_set.all(), instance=self.object)
		ctx = super(CustomerUpdate, self).get_context_data(**kwargs)
		ctx['date'] = self.object.get_formatted_date()
		if self.request.POST:
			ctx['message'] = messages.add_message(self.request, messages.SUCCESS, 'SUCCESS: Customer updated')	
		else:
			ctx['message'] = messages.add_message(self.request, messages.ERROR, 'ERROR: Customer not updated')	
		ctx['inlines'] = userList
		return ctx 

	def post(self, request, *args, **kwargs):
		if self.pk_url_kwarg:
			self.object = self.get_object()
			form = self.form_class(request.POST, instance=self.object)
			inlines = self.userFormSet(request.POST, request.FILES, instance=self.object)
		if form.is_valid() and inlines.is_valid():
			return self.form_valid(form, inlines)
		else:
			return self.form_invalid(form, inlines)

	def form_valid(self, form, inlines):
		if not self.object:
			self.object = form.save()
		else:
			form.save()
		inlines.instance = self.object
		inlines.save()
		"""executable = os.path.join('/home/nick/Desktop/key/static', 'update_keycodes.bat')
		p = subprocess.Popen([executable, self.object.name, str(self.object.keycodes_expire)])"""
		return HttpResponseRedirect('/userKeyGen/')

	def form_invalid(self, form, inlines):
		return self.render_to_response(self.get_context_data(form=form, inlines=inlines))

class CustomerDelete(generic.DeleteView):
	model = Customer
	success_url = reverse_lazy('index')
	
	def get_context_data(self, **kwargs):
		ctx = super(CustomerDelete, self).get_context_data(**kwargs)
		ctx['object'] = CustomerDelete()
		if self.request.POST:		
			ctx['message'] = messages.add_message(self.request, messages.SUCCESS, 'SUCCESS: Customer deleted')
		else:
			ctx['message'] = messages.add_message(self.request, messages.SUCCESS, 'ERROR: Customer not deleted')

class KeycodeRenewal(generic.UpdateView):
	model = Customer
	form_class = KeycodeRenewalForm
	userFormSet = inlineformset_factory(Customer, User, fields=['expiration_date'], extra=0)
	template_name_suffix = '_gma'
	
	def get_context_data(self, **kwargs):
		userList = self.userFormSet(queryset = self.object.user_set.all(), instance=self.object)
		ctx = super(KeycodeRenewal, self).get_context_data(**kwargs)
		ctx['users'] = userList
		return ctx

	def form_valid(self, form):
		if form.is_valid():
			for u in self.object.user_set.all():
				u.expiration_date = self.object.keycodes_expire
				u.save(update_fields=['expiration_date'])
				form.save()
			try:			
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh.connect('edge-qa2', username = 'bts', password = 'BT5u53r')
				"""windowscmd = 'C:\\Windows\\System32\\cmd.exe /c'
				btscmd = "C:\\edge\\current\\btscmd.exe logon RENEW -keyfile:\\\\10.96.18.41\\groups\\keys\\bts_private.pem -pass:bluetradesys"
				stdin, stderr, stdout = ssh.exec_command(windowscmd + ' ' + btscmd + ' ' + "-source:http://" + self.object.name + "/config/ -exp:"+ self.object.get_formatted_date() + " > ./"
									+ self.object.name + "-logon.conf")
				print stdout.read()
				stdin,stderr,stdout = ssh.exec_command(windowscmd + "plink.exe -i bts.ppk bts@" + self.object.name + " 'hg add ./wwwroot/config/logon.conf'")
				print stdout.read()
				stdin,stderr,stdout = ssh.exec_command(windowscmd + "plink.exe -i bts.ppk bts@" + self.object.name + " \"hg commit -m 'new' ./wwwroot/config/logon.conf\"")
				print stdout.read()
				stdin,stderr,stdout = ssh.exec_command(windowscmd + "pscp -i bts.ppk .\\"+ self.object.name + "-logon.conf bts@" + self.object.name + ":./wwwroot/config/logon.conf")
				print stdout.read()
				stdin,stderr,stdout = ssh.exec_command(windowscmd + "plink.exe -i bts.ppk bts@" + self.object.name + " 'cd edge/current && ./btscmd configcheck'")
				print stdout.read()
				time.sleep(5)
				stdin,stderr,stdout = ssh.exec_command(windowscmd + "del .\\" + self.object.name + "-logon.conf")"""
				stdin,stderr,stdout = ssh.exec_command("cd ~/edge/current/ && ./btscmd logon RENEW -keyfile:/home/bts/bts_private.pem -pass:bluetradesys -source:http://localhost/config/ -expiration:"+self.object.get_formatted_date())
				print stdin,stderr,stdout
			except paramiko.AuthenticationException:
				print "authenticate"
				sys.exit(1)
			"""windowscmd = "C:\\Windows\\System32\\cmd.exe /c"
			btscmd = "C:\\edge\\current\\btscmd.exe logon RENEW -keyfile:\\\\10.96.18.41\\groups\\keys\\bts_private.pem -pass:bluetradesys"
			command = "%s %s -source:http://%s/config/ -exp:%s > ./%s-logon.conf"%(windowscmd, btscmd, self.object, self.object.keycodes_expire, self.object)
			subprocess.call(command.split(), shell=False)"""
			"""command = "%s plink.exe -i bts.ppk bts@%s 'hg add ./wwwroot/config/logon.conf'"%(windowscmd, self.object)
			subprocess.call(command.split(), shell=False)
			command = "%s plink.exe -i bts.ppk bts@%s \"hg commit -m 'new' ./wwwroot/config/logon.conf\""%(windowscmd, self.object)
			subprocess.call(command.split(), shell=False)
			command = "%s pscp -i bts.ppk .\%s-logon.conf bts@%s:./wwwroot/config/logon.conf"%(windowscmd, self.object, self.object)
			subprocess.call(command.split(), shell=False)
			command = "%s plink.exe -i bts.ppk bts@%s 'cd edge/current && ./btscmd configcheck'"%(windowscmd, self.object)
			subprocess.call(command.split(), shell=False)
			time.sleep(5)
			command = "%s del .\%s-logon.conf"%(windowscmd, self.object)"""
			return HttpResponseRedirect('/userKeyGen/customer/'+str(self.object.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))
