# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quoter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_quote', to='user_app.User')),
            ],
            managers=[
                ('quoteManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='join',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='quote_app.Quote'),
        ),
        migrations.AddField(
            model_name='join',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='user_app.User'),
        ),
    ]