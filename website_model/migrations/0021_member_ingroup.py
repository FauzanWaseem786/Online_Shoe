# Generated by Django 2.2.1 on 2020-07-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_model', '0020_auto_20200714_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Ingroup',
            field=models.BooleanField(default=False),
        ),
    ]
