# Generated by Django 3.0 on 2020-02-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0002_auto_20200201_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='Unknown', max_length=10),
        ),
    ]
