from django.shortcuts import render
from django.views.generic.list import ListView

from content.models import Shortcuts

class ContentView(ListView):
    model = Shortcuts
    template_name = 'index.html'

