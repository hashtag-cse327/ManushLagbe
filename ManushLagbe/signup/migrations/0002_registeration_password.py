# Generated by Django 2.0.13 on 2019-07-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeration',
            name='password',
            field=models.CharField(default=50, max_length=100),
            preserve_default=False,
        ),
    ]
