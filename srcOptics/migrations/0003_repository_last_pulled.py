# Generated by Django 2.0.10 on 2019-03-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0002_auto_20190318_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='last_pulled',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]