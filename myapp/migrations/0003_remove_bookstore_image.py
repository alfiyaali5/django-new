# Generated by Django 5.0 on 2024-01-27 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_bookstore_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstore',
            name='image',
        ),
    ]