# Generated by Django 3.0 on 2020-02-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0006_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
