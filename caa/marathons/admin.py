from django.contrib import admin
from caa.marathons.models import Marathon, Event

class EventInline(admin.TabularInline):
	model = Event

class MarathonAdmin(admin.ModelAdmin):
	inlines = [
		EventInline,
	]

admin.site.register(Marathon, MarathonAdmin)
