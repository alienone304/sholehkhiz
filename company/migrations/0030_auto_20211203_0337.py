# Generated by Django 3.2 on 2021-12-03 00:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0029_auto_20211203_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintmodel',
            name='complained_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 0, 7, 52, 325016, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaintmodel',
            name='picture',
            field=models.ImageField(blank=True, default='cataloges/default/default.jpeg', null=True, upload_to='complaint/'),
        ),
        migrations.AlterField(
            model_name='contactusmodel',
            name='contacted_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 3, 0, 7, 52, 324089, tzinfo=utc)),
        ),
    ]
