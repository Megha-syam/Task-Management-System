# Generated by Django 4.1.13 on 2024-04-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskshow',
            name='deadline',
            field=models.DateField(max_length=100),
        ),
    ]