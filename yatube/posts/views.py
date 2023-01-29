from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse('Главная страница')

def group_posts(response, pk):
    return HttpResponse('Какой текст не принципиально, тут должно быть что-то интересное.')