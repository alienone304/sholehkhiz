# Generated by Django 3.2 on 2021-11-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productsmodel_cataloge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='cataloge',
            field=models.FileField(default='cataloges/default/default.jpeg', upload_to='cataloges/'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='picture',
            field=models.ImageField(default='products/default/default.jpeg', upload_to='products/'),
        ),
    ]
