# Generated by Django 2.2.1 on 2020-07-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_model', '0010_auto_20200712_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Email',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='ordr',
            name='email_id',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
