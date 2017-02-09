from django.contrib import admin
from .models import *

#
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'master']
#     list_filter = ('first_name', 'phone',)
#
#     # search_fields = ['last_name']
#     # list_display = [field.first_name for field in Course.meta.fields]
#     # inlines = [FieldMappingInline]
#     # fields = []
#     #  search_fields = ('last_name',)
#
#     class Meta:
#         model = Client


# admin.site.register(Client, ClientAdmin)


class MasterAdmin(admin.ModelAdmin):
    list_display = ['master_photo', 'full_name']

    class Meta:
        model = Master


# admin.site.register(Master)
# admin.site.register(Work_Time)
