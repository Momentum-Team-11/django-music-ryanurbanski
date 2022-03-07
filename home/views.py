from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/welcome.html'


def home(request):
    return render(request, 'home/welcome.html', {})
