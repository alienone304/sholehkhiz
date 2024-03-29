# Generated by Django 3.2 on 2021-12-02 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20211202_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 15, 17, 21, 663586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='last_message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 15, 17, 21, 662634, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 15, 17, 21, 662581, tzinfo=utc)),
        ),
    ]
