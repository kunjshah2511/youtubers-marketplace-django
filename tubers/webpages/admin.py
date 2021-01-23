from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def  myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display=('id', 'myphoto', 'first_name', 'role')
    list_display_links=('first_name',)#as this is list , only one item is not allowed so just put a coma after the item
    search_fields=('first_name','role')
    list_filter=('role',)#as this is list , only one item is not allowed so just put a coma after the item

# Register your models here.
admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)