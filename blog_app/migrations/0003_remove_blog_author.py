# Generated by Django 4.0.5 on 2022-06-13 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]