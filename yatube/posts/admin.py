from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk','text', 'pub_date', 'author', 'group',) 
    # Позволит изменять поле group в любом посте без лишних движений
    # мышкой, прямо из списка постов
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)
# Register your models here.
