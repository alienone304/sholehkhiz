# Generated by Django 3.2 on 2021-12-07 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20211203_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 10, 32, 27, 118519, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='last_message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 10, 32, 27, 117572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 10, 32, 27, 117521, tzinfo=utc)),
        ),
    ]
