# Generated by Django 2.0.10 on 2019-03-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0003_repository_last_pulled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.TextField(db_index=True, max_length=32, unique=True),
        ),
    ]