# Generated by Django 2.2 on 2020-08-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200801_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
