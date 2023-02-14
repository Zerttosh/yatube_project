from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='main_page'),
    # Страница со списком сортов мороженого
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
