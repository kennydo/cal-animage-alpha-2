from django.contrib import admin
from caa.schedules.models import Building, Location, Schedule, Showing, Weekly

class ShowingInline(admin.TabularInline):
    model = Showing
    
class WeeklyInline(admin.StackedInline):
    model= Weekly

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'map_url')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('building', 'room_number')

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        ShowingInline,
        WeeklyInline,
    ]
    
#class ShowingAdmin(admin.ModelAdmin):
#   list_display = ('title', 'location', 'date', 'start_time', 'end_time', 'schedule')
#   list_filter = ('schedule',)

#class WeeklyAdmin(admin.ModelAdmin):
#   list_display = ('title', 'schedule')
#   list_filter = ('schedule',)

admin.site.register(Building, BuildingAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Schedule, ScheduleAdmin)

#admin.site.register(Showing, ShowingAdmin)
#admin.site.register(Weekly, WeeklyAdmin)
