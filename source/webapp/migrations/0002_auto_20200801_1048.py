# Generated by Django 2.2 on 2020-08-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mail',
            field=models.CharField(max_length=254, verbose_name='email'),
        ),
    ]
