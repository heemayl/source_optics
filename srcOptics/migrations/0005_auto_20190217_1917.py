# Generated by Django 2.1.5 on 2019-02-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0004_auto_20190217_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='username',
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.TextField(max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.TextField(max_length=256, unique=True),
        ),
    ]
