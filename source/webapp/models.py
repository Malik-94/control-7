from django.db import models

# Create your models here.


class Poll(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text



class Choice(models.Model):
    option_text = models.TextField(max_length=300, null=True, blank=True, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='text_poll', on_delete=models.CASCADE , verbose_name='Опрос')


    def __str__(self):
        return self.option_text