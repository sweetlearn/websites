from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from .models import Question

def home(request):
    template_name = "index.html"
    return render(request, template_name, context=None)


def add(request):
    template_name = "result.html"

    return render(request, template_name, context=None)
