# Generated by Django 5.0.3 on 2024-04-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='insuaranceCompany',
            new_name='insuranceCompany',
        ),
    ]
