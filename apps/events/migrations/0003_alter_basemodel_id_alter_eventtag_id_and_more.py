# Generated by Django 5.0.1 on 2024-06-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='id',
            field=models.UUIDField(default='4a458960-23ae-4d4d-82cf-b3c783fbb0a5', editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='eventtag',
            name='id',
            field=models.UUIDField(default='92676ed1-ff1b-401b-aa3e-a380daa5f5f4', editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='id',
            field=models.UUIDField(default='eecf61d8-aa9a-4bd9-8f10-34ba5be2158d', editable=False, help_text='Unique identifier for this object.', primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
