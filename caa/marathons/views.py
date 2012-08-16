from django.http import Http404
from django.views.generic import DetailView

from caa.marathons.models import Marathon

class MarathonDetail(DetailView):
    model = Marathon
    template_name = 'marathon_detail.html'
    context_object_name = 'marathon'

    def get_object(self, queryset=None):
        """
        Returns the marathon the view is displaying.
        """
        year = self.kwargs.get('year', None)
        semester = self.kwargs.get('semester', '')[:2].upper()

        try:
            obj = Marathon.objects.get(year=year, semester=semester)
        except Marathon.DoesNotExist:
            raise Http404("No object found")
        return obj
