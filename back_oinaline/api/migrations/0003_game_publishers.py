# Generated by Django 2.2 on 2022-05-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_screenshot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='publishers',
            field=models.ManyToManyField(to='api.Publisher'),
        ),
    ]