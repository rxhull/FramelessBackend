# Generated by Django 3.2.3 on 2021-06-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website',
            old_name='icon',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='website',
            name='date_created',
        ),
        migrations.AddField(
            model_name='website',
            name='company',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='duration',
            field=models.TextField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='location',
            field=models.TextField(default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='type',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
