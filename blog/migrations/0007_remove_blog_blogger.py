# Generated by Django 2.0.7 on 2018-07-18 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_blogger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blogger',
        ),
    ]
