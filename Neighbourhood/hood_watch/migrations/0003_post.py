# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood_watch', '0002_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood_watch.User')),
            ],
        ),
    ]
