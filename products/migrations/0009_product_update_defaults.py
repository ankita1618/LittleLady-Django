# Generated by Django 3.1.2 on 2020-11-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201111_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='update_defaults',
            field=models.BooleanField(default=False),
        ),
    ]
