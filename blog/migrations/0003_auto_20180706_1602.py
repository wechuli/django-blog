# Generated by Django 2.0.7 on 2018-07-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180706_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogauthor',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.RenameField(
            model_name='blogauthor',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='blogauthor',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogauthor',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
