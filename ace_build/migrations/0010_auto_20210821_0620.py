# Generated by Django 3.1.7 on 2021-08-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_build', '0009_auto_20210820_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optimization',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
