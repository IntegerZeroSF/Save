# Generated by Django 3.0.3 on 2020-02-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save', '0012_auto_20200212_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
