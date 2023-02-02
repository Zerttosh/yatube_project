from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template_index = 'posts/index.html'
    return render(request, template_index)


def group_posts(request, slug):
    template = 'posts/groups.html'
    return render(request, template)