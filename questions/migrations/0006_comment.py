# Generated by Django 2.1.2 on 2018-11-06 19:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20181106_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_data', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания комментария')),
                ('text', models.TextField(blank=True, verbose_name='Комментарий')),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
    ]