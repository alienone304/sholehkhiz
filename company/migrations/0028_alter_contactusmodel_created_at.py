# Generated by Django 3.2 on 2021-12-02 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0027_alter_contactusmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 15, 17, 21, 651324, tzinfo=utc)),
        ),
    ]
