# Generated by Django 4.1.13 on 2024-03-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_register_signupdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupdetails',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
