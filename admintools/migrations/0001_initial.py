# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataQualityIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=300)),
                ('alert', models.CharField(max_length=50)),
                ('issue', models.CharField(choices=[('missing-phone', 'Missing Phone Number'), ('missing-email', 'Missing Email'), ('missing-address', 'Missing Postal Address'), ('missing-photo', 'Missing Photo'), ('no-memberships', 'No Memberships'), ('unmatched-person', 'Unmatched Person'), ('no-actions', 'Missing Actions'), ('no-sponsors', 'Missing Sponsors'), ('no-versions', 'Missing Versions'), ('unmatched-person-sponsor', 'Sponsor With Unmatched Person'), ('unmatched-org-sponsor', 'Sponsor With Unmatched Organization'), ('missing-bill', 'Missing Bill'), ('missing-voters', 'Missing Voters'), ('missing-counts', 'Missing Counts'), ('bad-counts', 'Bad Counts'), ('unmatched-voter', 'Unmatched Voter')], max_length=150)),
                ('reporter', models.CharField(blank=True, max_length=300)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('jurisdiction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataquality_issues', to='core.Jurisdiction')),
            ],
            options={
                'db_table': 'opencivicdata_dataqualityissue',
            },
        ),
        migrations.AlterIndexTogether(
            name='dataqualityissue',
            index_together=set([('alert', 'issue')]),
        ),
    ]
