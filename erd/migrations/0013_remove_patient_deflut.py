# Generated by Django 4.2.4 on 2023-12-13 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0012_alter_patient_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='deflut',
        ),
    ]
