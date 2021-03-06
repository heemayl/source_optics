# Generated by Django 2.2.2 on 2019-06-25 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(db_index=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.TextField(db_index=True, max_length=256)),
                ('commit_date', models.DateTimeField(db_index=True, null=True)),
                ('author_date', models.DateTimeField(null=True)),
                ('subject', models.TextField(db_index=True, max_length=256)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='source_optics.Author')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=256, null=True)),
                ('path', models.TextField(db_index=True, max_length=256, null=True)),
                ('ext', models.TextField(max_length=32, null=True)),
                ('binary', models.BooleanField(default=False)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LoginCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
                ('username', models.TextField(max_length=32)),
                ('password', models.TextField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, unique=True)),
                ('admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('last_scanned', models.DateTimeField(blank=True, null=True)),
                ('last_rollup', models.DateTimeField(blank=True, null=True)),
                ('earliest_commit', models.DateTimeField(blank=True, null=True)),
                ('last_pulled', models.DateTimeField(blank=True, null=True)),
                ('url', models.TextField(max_length=256, unique=True)),
                ('name', models.TextField(db_index=True, max_length=32, unique=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('cred', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source_optics.LoginCredential')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='source_optics.Organization')),
            ],
            options={
                'verbose_name_plural': 'repositories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_index=True, max_length=64, null=True)),
                ('repos', models.ManyToManyField(blank=True, related_name='tagged_repos', to='source_optics.Repository')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(db_index=True, null=True)),
                ('interval', models.TextField(choices=[('DY', 'Day'), ('WK', 'Week'), ('MN', 'Month')], db_index=True, max_length=5)),
                ('lines_added', models.IntegerField(blank=True, null=True)),
                ('lines_removed', models.IntegerField(blank=True, null=True)),
                ('lines_changed', models.IntegerField(blank=True, null=True)),
                ('commit_total', models.IntegerField(blank=True, null=True)),
                ('files_changed', models.IntegerField(blank=True, null=True)),
                ('author_total', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='source_optics.Author')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='source_optics.File')),
                ('repo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repo', to='source_optics.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='repository',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='source_optics.Tag'),
        ),
        migrations.CreateModel(
            name='FileChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=256, null=True)),
                ('path', models.TextField(db_index=True, max_length=256, null=True)),
                ('ext', models.TextField(max_length=32)),
                ('binary', models.BooleanField(default=False)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
                ('commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='source_optics.Commit')),
                ('repo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filechange_repo', to='source_optics.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='changes',
            field=models.ManyToManyField(related_name='changes', to='source_optics.FileChange'),
        ),
        migrations.AddField(
            model_name='file',
            name='repo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_repo', to='source_optics.Repository'),
        ),
        migrations.AddField(
            model_name='commit',
            name='files',
            field=models.ManyToManyField(to='source_optics.File'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repos', to='source_optics.Repository'),
        ),
        migrations.AddField(
            model_name='author',
            name='repos',
            field=models.ManyToManyField(related_name='author_repos', to='source_optics.Repository'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['interval', 'author', 'repo', 'file', 'start_date'], name='rollup1'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['start_date', 'interval', 'repo', 'author'], name='author_rollup'),
        ),
        migrations.AlterUniqueTogether(
            name='statistic',
            unique_together={('start_date', 'interval', 'repo', 'author', 'file')},
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['commit_date', 'author', 'repo'], name='source_opti_commit__69e2b7_idx'),
        ),
    ]
