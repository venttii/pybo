# Generated by Django 3.1.3 on 2021-01-27 12:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0014_auto_20210127_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default=None, max_length=15, null=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2021, 1, 27, 12, 23, 7, 758410, tzinfo=utc), null=True)),
                ('post', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.board')),
            ],
        ),
    ]
