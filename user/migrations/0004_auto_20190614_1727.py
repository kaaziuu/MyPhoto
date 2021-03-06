# Generated by Django 2.2.2 on 2019-06-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190611_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile/'),
        ),
    ]
