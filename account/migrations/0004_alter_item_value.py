# Generated by Django 4.2.5 on 2023-09-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_server_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
