# Generated by Django 2.0.10 on 2019-03-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcOptics', '0009_statistic_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='attributes',
            field=models.TextField(choices=[('commit_total', 'Total Commits'), ('lines_added', 'Lines Added'), ('lines_removed', 'Lines Removed'), ('lines_changed', 'Lines Changed')], max_length=24),
        ),
    ]
