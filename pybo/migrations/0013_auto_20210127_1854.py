# Generated by Django 3.1.3 on 2021-01-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0012_auto_20210127_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='notice',
            field=models.BooleanField(default=False, null=True),
        ),
    ]