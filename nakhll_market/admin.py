from typing import Dict, Optional
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.utils.timezone import localtime

from nakhll import utils
from .models import (LandingPageSchema, Category, ShopPageSchema,
                     LandingImage, LandingPage,
                     Shop,
                     Product, ProductBanner, Profile,
                     Alert, DashboardBanner, Slider)
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Permission

admin.site.site_header = 'مدیریت بازار نخل '

# enable django permission setting in admin panel to define custom permissions
admin.site.register(Permission)


ModelAdmin.construct_change_message = (
    lambda self, request, form, formsets, add:
    utils.construct_change_message(request, form, formsets, add)
)


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = (
        'FK_User',
        'MobileNumber',
        'BrithDay',
        'UserReferenceCode',
        'Point')
    readonly_fields = ('UserReferenceCode',)
    list_filter = ('BrithDay',)
    ordering = ['ID', 'BrithDay', 'Point', 'UserReferenceCode']
    search_fields = ('MobileNumber', 'UserReferenceCode',)
# -------------------------------------------------
# market admin panel


@admin.register(Shop)
class ShopAdmin(ModelAdmin):
    list_display = (
        'Title',
        'Slug',
        'City',
        'State',
        'Point',
        'DateCreate',
        'Available',
        'Publish',
    )
    list_filter = (
        'City',
        'State',
        'Publish',
        'Available',
        'DateCreate',
        'DateUpdate')
    search_fields = ('Title', 'Slug')
    ordering = ['ID', 'DateCreate', 'DateUpdate']
    raw_id_fields = ('FK_ShopManager', )

    def DateCreate(self, obj):
        return localtime(obj.DateCreate).strftime('%Y-%m-%d %H:%M:%S')

    def DateUpdate(self, obj):
        return localtime(obj.DateUpdate).strftime('%Y-%m-%d %H:%M:%S')
# -------------------------------------------------


class ProductBannerInline(admin.StackedInline):
    model = ProductBanner
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'Title',
        'Slug',
        'Bio',
        'Price',
        'Status',
        'DateCreate',
        'Publish')
    list_filter = ('Status', 'Publish', 'Available', 'DateCreate', 'DateUpdate')
    search_fields = ('Title', 'Slug', 'Description', 'Bio', 'Story')
    ordering = ['ID', 'DateCreate', 'DateUpdate']
    inlines = [ProductBannerInline, ]

    def DateCreate(self, obj):
        return localtime(obj.DateCreate).strftime('%Y-%m-%d %H:%M:%S')

    def DateUpdate(self, obj):
        return localtime(obj.DateUpdate).strftime('%Y-%m-%d %H:%M:%S')

    def change_view(
            self, request: HttpRequest, object_id: str, form_url: str = '',
            extra_context: Optional[Dict[str, bool]] = None) -> HttpResponse:
        if request.user.groups.filter(name='Photo-compress').exists():
            self.fields = ('Image', 'NewImage')
        else:
            self.fields = None
        return super().change_view(request, object_id,
                                   form_url=form_url, extra_context=extra_context)
# -------------------------------------------------


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'order',
        'slug',
        'description',
        'parent',
        'available')
    list_filter = ('parent', 'available')
    ordering = ('-parent', 'id', )

# -------------------------------------------------
# Alert admin panel


@admin.register(Alert)
class AlertAdmin(ModelAdmin):
    list_display = ('Part', 'Slug', 'Seen', 'DateCreate', 'Description',)
    list_filter = ('Seen', 'Status', 'DateCreate', 'DateCreate', 'DateUpdate')
    search_fields = ('FK_Field', 'Description', 'Content',)
    ordering = ['id', 'DateCreate', ]

    def DateCreate(self, obj):
        return localtime(obj.DateCreate).strftime('%Y-%m-%d %H:%M:%S')

    def DateUpdate(self, obj):
        return localtime(obj.DateUpdate).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(ProductBanner)
class ProductBanner(ModelAdmin):
    list_display = ('FK_Product', 'Title', 'DateCreate', 'DateUpdate')
    list_filter = ('FK_Product', 'Title', 'DateCreate', 'DateUpdate')
    search_fields = ('FK_Product__Title',)
    ordering = ('DateCreate',)

    def DateCreate(self, obj):
        return localtime(obj.DateCreate).strftime('%Y-%m-%d %H:%M:%S')

    def DateUpdate(self, obj):
        return localtime(obj.DateUpdate).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(DashboardBanner)
class DashboardBannerAdmin(ModelAdmin):
    list_display = (
        'image',
        'url',
        'staff_user',
        'created_datetime',
        'publish_status')
    list_filter = ('staff_user', 'created_datetime', 'publish_status')
    search_fields = ('url',)
    ordering = ['id', 'created_datetime', 'publish_status']

    def created_datetime(self, obj):
        return localtime(obj.created_datetime).strftime('%Y-%m-%d %H:%M:%S')
    # inlines=[AttrProductInline, ProductBannerInline, ProductMovieInline]


@admin.register(LandingPageSchema)
class LandingPageSchemaAdmin(ModelAdmin):
    list_display = (
        'component_type',
        'title',
        'subtitle',
        'image',
        'url',
        'data',
        'order',
        'publish_status')
    list_filter = ('publish_status', 'created_datetime', 'order')
    search_fields = ('title', 'component_type', 'subtitle', 'url', 'data')
    ordering = ['publish_status', 'created_datetime']

    def created_datetime(self, obj):
        return localtime(obj.created_datetime).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(ShopPageSchema)
class ShopPageSchemaAdmin(ModelAdmin):
    list_display = (
        'shop',
        'component_type',
        'title',
        'subtitle',
        'image',
        'url',
        'data',
        'order',
        'publish_status')
    list_filter = ('shop', 'publish_status', 'created_datetime', 'order')
    search_fields = (
        'shop',
        'title',
        'component_type',
        'subtitle',
        'url',
        'data')
    ordering = ['publish_status', 'created_datetime']

    def created_datetime(self, obj):
        return localtime(obj.created_datetime).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(LandingPage)
class LandingPageAdmin(ModelAdmin):
    list_display = ('slug', 'status', 'staff', 'created_at', 'updated_at')
    list_filter = ('status', )
    search_fields = ('slug', 'page_data')
    ordering = ['created_at']

    def created_datetime(self, obj):
        return localtime(obj.created_datetime).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(LandingImage)
class LandingImageAdmin(ModelAdmin):
    list_display = (
        'image',
        'staff',
        'created_at',
        'updated_at',
        'landing_page')
    list_filter = ('landing_page', )
    ordering = ['created_at']

    def created_datetime(self, obj):
        return localtime(obj.created_datetime).strftime('%Y-%m-%d %H:%M:%S')


@admin.register(Slider)
class SliderAdmin(ModelAdmin):
    list_display = ('Title', 'Description', 'Location', 'DateCreate', 'Publish')
    list_filter = ('Location', 'DateCreate', 'DtatUpdate', 'Publish')
    ordering = ['DateCreate', 'id', 'Publish', 'Title', 'Location']

    def DateCreate(self, obj):
        return localtime(obj.DateCreate).strftime('%Y-%m-%d %H:%M:%S')

    def DtatUpdate(self, obj):
        return localtime(obj.DtatUpdate).strftime('%Y-%m-%d %H:%M:%S')
