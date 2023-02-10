from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template_index = 'posts/index.html'
    poem = ('Вчера Крокодил<br>улыбнулся так злобно,<br>Что мне до сих '
            'пор<br>за него неудобно.<br><i>Рената Муха</i>'
            )
    context = {
        'title': 'Главная страница',
        'text': 'Это главная страница проекта Yatube',
        'poem': poem,
    }
    return render(request, template_index, context)


def group_posts(request, slug):
    template_group_posts = 'posts/group_list.html'
    context = {
        'title': 'Группы Yatube',
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template_group_posts, context)