# Generated by Django 2.1.2 on 2018-11-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20181106_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answers_count',
            new_name='comments_count',
        ),
    ]
