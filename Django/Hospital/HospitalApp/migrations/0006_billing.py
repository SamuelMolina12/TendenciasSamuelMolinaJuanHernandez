# Generated by Django 5.0.3 on 2024-04-30 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0005_delete_billing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patientName', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('policyNumber', models.IntegerField()),
                ('termPolicy', models.CharField(max_length=30)),
                ('cost', models.FloatField()),
                ('totalPay', models.FloatField()),
                ('doctorName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.employer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.order')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.patient')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HospitalApp.policy')),
            ],
        ),
    ]
