# Generated by Django 3.2 on 2021-11-28 13:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 17, 6, 21, 813569)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 17, 6, 21, 812710)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='superuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
