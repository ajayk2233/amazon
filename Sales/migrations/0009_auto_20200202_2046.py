# Generated by Django 3.0 on 2020-02-03 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0008_auto_20200202_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
