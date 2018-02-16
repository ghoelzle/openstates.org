# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0001_initial'),
        ('dataquality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueResolverPatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=100)),
                ('old_value', models.CharField(blank=True, max_length=2250)),
                ('new_value', models.CharField(max_length=2250)),
                ('category', models.CharField(choices=[('name', 'Name'), ('address', 'Address'), ('voice', 'Phone'), ('email', 'Email'), ('image', 'Photo')], max_length=500)),
                ('alert', models.CharField(choices=[('warning', 'Missing Value'), ('error', 'Wrong Value')], max_length=500)),
                ('note', models.TextField(blank=True)),
                ('source', models.URLField(blank=True, max_length=2250)),
                ('reporter_email', models.EmailField(blank=True, max_length=254)),
                ('reporter_name', models.CharField(blank=True, max_length=500)),
                ('applied_by', models.CharField(max_length=205)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('jurisdiction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_resolver_patches', to='core.Jurisdiction')),
            ],
        ),
    ]
