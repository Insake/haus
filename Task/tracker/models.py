from django.db import models
from .constants import *

class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название категории')
    date_created = models.DateTimeField(auto_now=True,verbose_name='Время создания')
    date_modified = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=9, verbose_name='Статус категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Task(models.Model):
    category_id = models.ForeignKey(Category,verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание')
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_TASK, max_length=6, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    done = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.title} до {self.deadline}'