# Generated by Django 2.0.7 on 2018-07-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180706_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthor',
            name='tag_line',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
