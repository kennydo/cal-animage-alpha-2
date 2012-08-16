from django.conf.urls import patterns, include, url
from django.contrib import admin

from caa import officers, schedules, marathons

admin.autodiscover()

urlpatterns = patterns('',
    # Current schedule
#    url(r'^schedules/current/$', schedules.views.CurrentSchedule.as_view(), name='caa_current_schedule'),
    
    # Previous schedule
#    url(r'^schedules/(?P<year>\d{4})/(?P<semester>Fall|Spring)/$', schedules.views.ScheduleDetail.as_view(), name='caa_schedule'),

    # Officers listing
    url(r'^officers/$', officers.views.OfficersByDepartment.as_view(), name='caa_officers'),

    # Previous marathon
    url(r'^marathons/(?P<year>\d{4})/(?P<semester>Fall|Spring)/$', marathons.views.MarathonDetail.as_view(), name='caa_marathon'),

    # Enable admin
    url(r'^admin/', include(admin.site.urls)),
)
