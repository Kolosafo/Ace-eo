# Generated by Django 3.1.7 on 2021-08-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_build', '0008_optimization_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optimization',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
