from django.contrib import admin
from .models import Customer, User

class UserInLine(admin.TabularInline):
    model = User
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['active', 'name', 'system', 'bill_amount', 'exchanges']}),
		('Dates', {'fields': ['due_date', 'invoice_date', 'keycodes_expire', 'paid_date']})
	]
	inlines = [UserInLine]
	list_display = ('name', 'system', 'bill_amount', 'invoice_date', 'due_date', 'paid_date', 'exchanges', 'keycodes_expire', 'active')
	ordering = ('name',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(User)


# Register your models here.
