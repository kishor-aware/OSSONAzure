# Generated by Django 3.1.7 on 2021-03-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptionsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
