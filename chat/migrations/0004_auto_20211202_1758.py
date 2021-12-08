# Generated by Django 3.2 on 2021-12-02 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20211128_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsessionmodel',
            name='last_message_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 17, 58, 32, 785016)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 17, 58, 32, 783946)),
        ),
    ]
