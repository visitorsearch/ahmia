# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import ahmia.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HiddenWebsite',
            fields=[
                ('url', models.URLField(unique=True, validators=[ahmia.models.validate_onion_url])),
                ('id', models.CharField(max_length=16, unique=True, serialize=False, primary_key=True, validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MaxLengthValidator(16)])),
                ('banned', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('md5', models.CharField(unique=True, max_length=32, validators=[django.core.validators.MinLengthValidator(32), django.core.validators.MaxLengthValidator(32)])),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HiddenWebsiteDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('relation', models.URLField(null=True, blank=True)),
                ('subject', models.TextField(null=True, blank=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('language', models.TextField(null=True, blank=True)),
                ('contactInformation', models.TextField(null=True, blank=True)),
                ('officialInfo', models.BooleanField(default=False)),
                ('about', models.ForeignKey(to='ahmia.HiddenWebsite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HiddenWebsitePopularity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clicks', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('public_backlinks', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('tor2web', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('about', models.ForeignKey(to='ahmia.HiddenWebsite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HiddenWebsiteStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('online', models.BooleanField(default=True)),
                ('about', models.ForeignKey(to='ahmia.HiddenWebsite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.TextField()),
                ('url', models.URLField(unique=True)),
                ('tor2web_url', models.URLField(unique=True)),
                ('text', models.TextField()),
                ('title', models.TextField()),
                ('h1', models.TextField()),
                ('h2', models.TextField()),
                ('crawling_session', models.TextField()),
                ('server_header', models.TextField()),
                ('date_inserted', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
