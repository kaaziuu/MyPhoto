# Generated by Django 2.2.2 on 2019-06-05 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='image/')),
                ('slug', models.SlugField(unique=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('like', models.BigIntegerField(default=0)),
                ('ILike', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date', '-author'],
            },
        ),
        migrations.CreateModel(
            name='FollowedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('u1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u1', to=settings.AUTH_USER_MODEL)),
                ('u2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]