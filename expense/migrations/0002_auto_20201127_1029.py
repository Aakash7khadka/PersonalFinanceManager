# Generated by Django 3.1.2 on 2020-11-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='bill',
            field=models.ImageField(blank=True, null=True, upload_to='bill/'),
        ),
    ]
