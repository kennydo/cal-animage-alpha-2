from django.contrib import admin
from caa.officers.models import Department, Officer

class OfficerAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'nickname','title', 'is_head']
    list_filter = ['department', 'is_head']

admin.site.register(Department)
admin.site.register(Officer, OfficerAdmin)
