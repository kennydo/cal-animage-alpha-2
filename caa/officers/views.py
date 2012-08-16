from django.views.generic import ListView

from caa.officers.models import Department

class OfficersByDepartment(ListView):
    model = Department
    template_name = 'officers_list.html'
    context_object_name = 'departments'
