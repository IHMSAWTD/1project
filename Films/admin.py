from django.contrib import admin
from .models import Film,Category


class HelpAdmin(admin.ModelAdmin):
    list_display = ['filmName','duration','created_at','country','rating','get_categories']



admin.site.register(Film,HelpAdmin)
admin.site.register(Category)

