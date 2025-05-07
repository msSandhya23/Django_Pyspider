from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class HtmlWithData(TemplateView):
    template_name = 'HtmlWithData.html'
    def get_context_data(self, **kwargs):
        EDCO = super().get_context_data(**kwargs)
        EDCO ['name'] = 'John Doe'
        EDCO['age'] = 30
        EDCO['city'] = 'New York'
        return EDCO