# Generated by Django 5.0.4 on 2024-05-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.TextField(max_length=1000),
        ),
    ]
