from django.contrib import admin

from .models import Route, RouteType, Photo


# Register your models here.

class RouteInline(admin.TabularInline):
    model = RouteType.routes.through


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('title', 'long', 'lat')


@admin.register(RouteType)
class RouteTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('routes',)
    inlines = [
        RouteInline,
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo',)
