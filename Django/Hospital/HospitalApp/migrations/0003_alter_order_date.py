# Generated by Django 5.0.3 on 2024-04-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0002_rename_doctorid_order_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
    ]
