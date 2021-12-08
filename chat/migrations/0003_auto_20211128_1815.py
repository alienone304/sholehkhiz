# Generated by Django 3.2 on 2021-11-28 14:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20211128_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='chatsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.chatsessionmodel'),
        ),
        migrations.AlterField(
            model_name='chatmessagemodel',
            name='message_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 18, 15, 1, 13259)),
        ),
        migrations.AlterField(
            model_name='chatsessionmodel',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 18, 15, 1, 12393)),
        ),
    ]