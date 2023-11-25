from contest.models import Contest
from django.shortcuts import render
from django.views.generic import TemplateView


def description(request):
    template = 'about/description.html'
    return render(request, template)


class Description(TemplateView):
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_claims'] = Contest.objects.count()
        return context
