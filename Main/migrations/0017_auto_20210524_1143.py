# Generated by Django 3.1.7 on 2021-05-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0016_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
