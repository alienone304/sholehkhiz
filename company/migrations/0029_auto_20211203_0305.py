# Generated by Django 3.2 on 2021-12-02 23:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0028_alter_contactusmodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('phone_number', models.CharField(max_length=264)),
                ('request', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='complaint/')),
                ('complained_at', models.DateTimeField(default=datetime.datetime(2021, 12, 2, 23, 35, 13, 846811, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='contactusmodel',
            name='created_at',
        ),
        migrations.AddField(
            model_name='contactusmodel',
            name='contacted_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 23, 35, 13, 845892, tzinfo=utc)),
        ),
    ]
