# Generated by Django 5.0.3 on 2024-04-16 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0010_rename_namediagnostic_diagnostichelp_diagnosticname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policy',
            old_name='policynumber',
            new_name='policyNumber',
        ),
    ]