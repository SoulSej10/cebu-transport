from django.contrib import admin
from .models import Request, BusTicket1, BusTicket2
# Register your models here.
#admin.site.register(Request)

@admin.register(BusTicket1)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'origin', 'destination', 'date','bus_type','total_fee' )
    ordering = ('fullname',)
    search_fields = ('fullname', 'bus_type', 'date')
@admin.register(BusTicket2)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'origin', 'destination', 'date','bus_type','total_fare' )
    ordering = ('fullname',)
    search_fields = ('fullname', 'bus_type', 'date')