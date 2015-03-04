from django.contrib import admin
from caa.konshuu.models import KonshuuEdition

class KonshuuEditionAdmin(admin.ModelAdmin):
	list_display = ['volume', 'issue']

admin.site.register(KonshuuEdition, KonshuuEditionAdmin)
