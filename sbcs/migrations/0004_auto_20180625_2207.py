# Generated by Django 2.0.4 on 2018-06-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbcs', '0003_auto_20180625_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='cod',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pack',
            name='cost_points',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pack',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]