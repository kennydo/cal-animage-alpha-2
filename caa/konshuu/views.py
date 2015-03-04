from django.views.generic import ListView

from caa.konshuu.models import KonshuuEdition

class KonshuuList(ListView):
    model = KonshuuEdition
    template_name = 'konshuu.html'
    context_object_name = 'editions'
