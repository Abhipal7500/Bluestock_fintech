from django.contrib import admin
from .models import IPOInfo

@admin.register(IPOInfo)
class IPOInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'price_band', 'listing_date', 'status', 'ipo_price', 'listing_price')
    search_fields = ('company_name', 'price_band', 'issue_type', 'listing_date')
    list_filter = ('status', 'listing_date', 'issue_type')
    ordering = ('-listing_date',)

# Alternatively, you can use admin.site.register if you don't want to use the @admin.register decorator
# admin.site.register(IPOInfo, IPOInfoAdmin)
