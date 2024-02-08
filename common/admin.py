from django.contrib import admin
from .models import Banner, Static, Service, Result, Contact, Review, SocialMedia


# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'image', 'link')
    list_display_links = ("subtitle", 'link')
    search_fields = ('subtitle',)


@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = ('student_count', 'universities_count', 'years_of_experienced', 'countries_count')
    list_display_links = ('student_count', 'universities_count')


@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'university', 'degree', 'image')
    list_display_links = ('full_name', 'university', 'degree')
    search_fields = ('full_name', 'university')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'degree', 'message')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'characterization', 'image')
    list_display_links = ('full_name',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('icon', 'social_name', 'order')
