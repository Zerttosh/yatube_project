from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

def index(request):
    template_index = 'posts/index.html'
    # poem = ('Вчера Крокодил<br>улыбнулся так злобно,<br>Что мне до сих '
    #         'пор<br>за него неудобно.<br><i>Рената Муха</i>'
    #         )
    # В переменную posts будет сохранена выборка из 10 объектов 
    # модели Post, отсортированных по полю pub_date по убыванию 
    # (от больших значений к меньшим)
    # Сортировка по свойству pub_date осуществляется по убыванию, от больших 
    # значений к меньшим (об этом говорит знак -): новые записи 
    # оказываются вверху выборки;
    posts = Post.objects.order_by('-pub_date')[:10]
    # Объекты класса Post, сохраняются в виде списка в переменной posts и 
    # передаются в словаре context под ключом 'posts'
    context = {
        # 'title': 'Главная страница',
        # 'text': 'Это главная страница проекта Yatube',
        # 'poem': poem,
        'posts': posts
    }
    return render(request, template_index, context)


def group_posts(request, slug):
    template_group_posts = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template_group_posts, context)