# Generated by Django 2.2.2 on 2019-06-08 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0003_auto_20190603_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='urlhash',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
    ]
