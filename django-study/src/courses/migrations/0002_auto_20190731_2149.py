# Generated by Django 2.0.7 on 2019-07-31 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='active',
        ),
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
    ]
