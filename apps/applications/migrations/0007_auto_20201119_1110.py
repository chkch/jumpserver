# Generated by Django 3.1 on 2020-11-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='attrs',
            field=models.JSONField(),
        ),
    ]