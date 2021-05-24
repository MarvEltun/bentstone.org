# Generated by Django 3.1.7 on 2021-05-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20210524_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('lang', models.CharField(default='EN', max_length=2)),
            ],
        ),
    ]
