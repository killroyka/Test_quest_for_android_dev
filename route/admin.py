from django.contrib import admin

from .models import Route, RouteType, Photo


# Register your models here.
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(RouteType)
class RouteTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
