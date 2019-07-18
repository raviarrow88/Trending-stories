# Generated by Django 2.2.3 on 2019-07-18 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField(blank=True, max_length=2000, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('content_type', models.CharField(blank=True, choices=[('T', 'text'), ('U', 'url'), ('I', 'image')], max_length=1, null=True)),
                ('start_comments', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('start_score', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(choices=[('N', 'new'), ('O', 'ok'), ('E', 'error')], default='N', max_length=1)),
                ('top_ten', models.BooleanField(default=False)),
                ('nsfw', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='services.Service')),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
                'ordering': ('-score',),
                'unique_together': {('service', 'code', 'date')},
            },
        ),
    ]
