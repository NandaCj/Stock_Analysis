from django.views import generic
from django.http import HttpResponse


class Home(generic.TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Nandha'
        return context

class Home_(generic.View):

    def get(self, request, *args, **kwargs):

        return HttpResponse('Understanding Views....')



