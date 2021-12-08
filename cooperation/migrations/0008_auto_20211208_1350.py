# Generated by Django 3.2 on 2021-12-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0007_alter_applicationmodel_resome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='age',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='cellphone_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='college_score',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='id_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='applicationmodel',
            name='phone_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='age',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='cellphone_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='fax_number',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='phone_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='sell_prediction_package',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='sell_prediction_radiator',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='sell_prediction_towerdryer',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='delegationrequestmodel',
            name='sell_prediction_waterheater',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='repairmanrequestmodel',
            name='age',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='repairmanrequestmodel',
            name='cellphone_number',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='repairmanrequestmodel',
            name='college_score',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='repairmanrequestmodel',
            name='phone_number',
            field=models.CharField(max_length=264),
        ),
    ]