# Generated by Django 3.2.8 on 2021-10-12 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0004_alter_todos_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todos',
            new_name='Todo',
        ),
    ]