from django.db import models
# Импортируется для обращения к модели User
from django.contrib.auth import get_user_model

# Обращение к модели User (встроена в Джанго)
User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return str(self.title)


# класс Post — это наследник класса Model из модуля models
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        # Ссылка на автора поста, на модель User
        User, 
        # Параметр on_delete=models.CASCADE обеспечивает связность данных: 
        # если из таблицы User будет удалён пользователь, то будут удалены 
        # все связанные с ним посты.
        on_delete=models.CASCADE,
        # Для создания в каждом объекте модели User свойства (posts), 
        # в котором будут храниться ссылки на все объекты модели Post, 
        # которые ссылаются на объект User 
        related_name='posts',
        )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        )
       
    def __str__(self):
        return self.text


# Create your models here.
