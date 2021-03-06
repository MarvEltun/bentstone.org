# Generated by Django 3.1.7 on 2021-05-24 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20210523_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
    ]
