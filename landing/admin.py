from django.contrib import admin
from .models import *
from .forms import ClientProfileForm


class MasterAdmin(admin.ModelAdmin):
    list_display = ['master_photo', 'full_name']

    class Meta:
        model = Master


class ClientProfileAdmin(admin.ModelAdmin):
    form = ClientProfileForm


admin.site.register(ClientProfile, ClientProfileAdmin)
admin.site.register(Address)
admin.site.register(Section)
