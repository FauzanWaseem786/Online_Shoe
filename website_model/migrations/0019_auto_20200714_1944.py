# Generated by Django 2.2.1 on 2020-07-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_model', '0018_auto_20200713_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Groups',
        ),
        migrations.AddField(
            model_name='group',
            name='Members',
            field=models.ManyToManyField(null=True, to='website_model.Member'),
        ),
    ]
