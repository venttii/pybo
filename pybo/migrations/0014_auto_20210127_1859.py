# Generated by Django 3.1.3 on 2021-01-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0013_auto_20210127_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='notice',
            field=models.BooleanField(default=False),
        ),
    ]
