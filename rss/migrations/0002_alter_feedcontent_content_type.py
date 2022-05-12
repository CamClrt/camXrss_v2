# Generated by Django 3.2.12 on 2022-05-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedcontent',
            name='content_type',
            field=models.CharField(choices=[('podcast', 'Podcast'), ('article', 'Article'), ('youtube', 'Youtube'), ('newsletter', 'Newsletter')], default='article', max_length=25),
        ),
    ]
