from django.http import Http404
from django.views.generic import DetailView

from caa.schedules.models import Schedule

class ScheduleDetail(DetailView):
    model = Schedule
    template_name = 'schedule_detail.html'
    context_object_name = 'schedule'

    def get_context_data(self, **kwargs):
        context = super(ScheduleDetail, self).get_context_data(**kwargs)
        context['all_schedules'] = Schedule.objects.all()
        return context

    def get_object(self, queryset=None):
        """
        Returns the schedule the view is displaying.
        """
        year = self.kwargs.get('year', None)
        semester = self.kwargs.get('semester', '')[:2].upper()

        try:
            obj = Schedule.objects.get(year=year, semester=semester)
        except Schedule.DoesNotExist:
            raise Http404("No object found")
        return obj

class CurrentSchedule(ScheduleDetail):
    def get_object(self, queryset=None):
        """
        Returns the latest schedule to display in the view.
        """
        try:
            obj = Schedule.objects.order_by('-year', 'semester')[0]
        except IndexError, e:
            raise Http404("No schedule found")
        return obj
