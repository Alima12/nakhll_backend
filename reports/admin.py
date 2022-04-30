from django.contrib import admin
from panel_admins.reports import reports_admin_site
# Register your models here.
from .models import InvoiceItemReport, InoviceProxy
from import_export.admin import ExportActionMixin


@admin.register(InvoiceItemReport, site=reports_admin_site)
class InvoiceItemReportAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('id', 'invoice_number', 'invoice_status', 'product_name', 'product_shop')
    list_filter = ( 'status',)
    ordering = ('-id',)

    # product items
    def product_name(self,obj):
        return obj.product.Title
    product_name.short_description = 'اسم محصول'

    def product_shop(self,obj):
        return obj.product.FK_Shop.Title
    product_shop.short_description = 'فروشگاه'



    # invoice items
    def invoice_status(self,obj):
        return obj.invoice.status
    invoice_status.short_description = 'وضعیت فاکتور'

    def invoice_number(self,obj):
        return obj.invoice.id
    invoice_number.short_description = 'شماره فاکتور'

    def get_queryset(self, request):
        qs = super(InvoiceItemReportAdmin, self).get_queryset(request)
        qs = qs.filter(invoice__status=InoviceProxy.Statuses.COMPLETED)
        return qs.select_related('invoice', 'product')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
