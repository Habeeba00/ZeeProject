# Generated by Django 4.2.4 on 2024-02-10 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diseases',
            options={'ordering': ['Deasesname']},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['patientId']},
        ),
        migrations.AlterModelOptions(
            name='login',
            options={'ordering': ['Userhandel']},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={'ordering': ['name']},
        ),
    ]
