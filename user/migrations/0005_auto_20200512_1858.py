# Generated by Django 3.0.6 on 2020-05-12 18:58

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190614_1727'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userdata',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
