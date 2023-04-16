from django.contrib import admin
from django.contrib.auth.models import Group

from .models import MenuItem


class MenuInline(admin.TabularInline):
    model = MenuItem
    fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title', )}
    extra = 3


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug', )
    prepopulated_fields = {'slug': ('title', )}
    inlines = (MenuInline, )


admin.site.unregister(Group)
