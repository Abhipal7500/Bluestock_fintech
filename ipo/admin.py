from django.contrib import admin
from .models import IPOInfo

@admin.register(IPOInfo)
class IPOInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'price_band', 'open', 'close', 'listing_date', 'status', 'ipo_price', 'listing_price', 'listing_gain', 'cmp', 'current_return')
    search_fields = ('company_name',)
    list_filter = ('status', 'listing_date')
