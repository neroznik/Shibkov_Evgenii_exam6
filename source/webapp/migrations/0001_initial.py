# Generated by Django 2.2 on 2020-08-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Unknown', max_length=40, verbose_name='Автор')),
                ('mail', models.EmailField(max_length=254, verbose_name='email')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('status', models.CharField(choices=[('active', ' Активно'), ('blocked', 'Заблокированно')], default='active', max_length=15, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
