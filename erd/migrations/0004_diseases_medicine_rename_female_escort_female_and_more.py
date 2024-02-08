# Generated by Django 4.2.4 on 2023-12-12 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0003_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('DiseasesID', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('Deasesname', models.CharField(max_length=100)),
                ('DeasesDiscription', models.CharField(max_length=100)),
                ('commen_symptoms', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('DrugID', models.IntegerField(max_length=50)),
                ('DrugName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('purpose_of_use', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100)),
                ('Duration_of_use', models.DateField()),
                ('number_of_times_day', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('expire_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='escort',
            old_name='feMale',
            new_name='Female',
        ),
        migrations.RemoveField(
            model_name='escort',
            name='id',
        ),
        migrations.AlterField(
            model_name='escort',
            name='EscortID',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('FirstName', models.CharField(max_length=100)),
                ('LasttName', models.CharField(max_length=100)),
                ('patientID', models.IntegerField(max_length=50, primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('PhoneNumber', models.IntegerField(max_length=100)),
                ('UserName', models.CharField(max_length=100)),
                ('ProfilePicture', models.ImageField(upload_to='photos%y%m%d')),
                ('Male', models.BooleanField(default=True)),
                ('Female', models.BooleanField(default=False)),
                ('DiseaseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erd.diseases')),
                ('EscortID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erd.escort')),
            ],
            options={
                'ordering': ['UserName'],
            },
        ),
    ]
