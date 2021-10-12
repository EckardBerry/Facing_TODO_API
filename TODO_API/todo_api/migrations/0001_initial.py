# Generated by Django 3.2.8 on 2021-10-12 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 10, 12, 19, 13, 52, 106808))),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('status', models.BooleanField(default='Incomplete')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
