from django.db import models

STATUS_CHOICES = [
    ('active', ' Активно'),
    ('blocked', 'Заблокированно'),
]


class Entry(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    mail = models.EmailField (max_length=254, null=False, blank= False,verbose_name='email')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Статус')

    def __str__(self):
        return "{}. {} {}".format(self.pk, self.author, self.mail)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'