# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_user_key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emailKey', models.CharField(max_length=300, null=True, blank=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog_user',
            name='keys',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
