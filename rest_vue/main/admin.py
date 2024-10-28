from django.contrib import admin
from main.models import InformationResource


@admin.register(InformationResource)
class InformationResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}