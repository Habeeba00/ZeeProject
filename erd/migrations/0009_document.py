# Generated by Django 4.2.4 on 2023-12-12 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0008_alter_escort_lastmodified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DrugName', models.CharField(max_length=50)),
                ('patientId', models.IntegerField()),
                ('prescriptionID', models.CharField(max_length=50)),
                ('exrays_test', models.ImageField(upload_to='photos%y%m%d')),
                ('diseasesId', models.IntegerField()),
                ('escortID', models.IntegerField()),
            ],
        ),
    ]
