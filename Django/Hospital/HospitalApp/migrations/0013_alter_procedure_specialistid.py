# Generated by Django 5.0.3 on 2024-04-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0012_specialist_alter_billing_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='specialistId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.specialist'),
        ),
    ]