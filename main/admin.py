from django.contrib import admin
from image_cropping import ImageCroppingMixin

from main.models import StaffModel, GalleryModel, NewsModel, BannerModel, ContactModel


@admin.register(NewsModel)
class NewsModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'content']


@admin.register(StaffModel)
class StaffModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'position', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'position']


@admin.register(GalleryModel)
class GalleryModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'text']