from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime
# from django.contrib.auth.models import User

# Create your models here.


class Diseases(models.Model):
    DiseasesID=models.CharField(primary_key=True,max_length=100)
    Deasesname=models.CharField(max_length=100)
    DeasesDiscription=models.CharField(max_length=100)
    commen_symptoms=models.CharField(max_length=100)



class Escort(models.Model):
    FirstName=models.CharField(max_length=100,null=False,blank=False)
    LasttName=models.CharField(max_length=100,null=False,blank=False)
    EscortID=models.IntegerField(primary_key=True,null=False,blank=False)
    Email=models.CharField(max_length=100,blank=False)
    Password=models.CharField(max_length=100,blank=False)
    PhoneNumber=models.CharField(null=False,blank=False,max_length=14)
    UserName=models.CharField(max_length=100,blank=False)
    ProfilePicture=models.ImageField(upload_to='photos%y%m%d')
    Male=models.BooleanField(default=True)
    Female=models.BooleanField(default=False)
    LastModified=models.DateTimeField(auto_now=True,null=False,blank=False)

    def __str__(self):
        return self.UserName
    class Meta:
        ordering=['UserName']




class patient(models.Model):
    FirstName=models.CharField(max_length=100,null=False,blank=False)
    LasttName=models.CharField(max_length=100,null=False,blank=False)
    patientID=models.IntegerField(null=False,primary_key=True,blank=False)
    # EscortID=models.IntegerField()
    DiseaseID=models.ForeignKey(Diseases,on_delete=models.CASCADE,blank=False)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100,blank=False)
    PhoneNumber=models.CharField(null=False,blank=False,max_length=100)
    UserName=models.CharField(max_length=100)
    ProfilePicture=models.ImageField(upload_to='photos%y%m%d')
    Male=models.BooleanField(default=True)
    Female=models.BooleanField(default=False)
    deflut=models.OneToOneField(Escort,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.UserName
    class Meta:
        ordering=['UserName']






class Medicine(models.Model):
    DrugID=models.IntegerField(null=False,blank=True)
    DrugName=models.CharField(primary_key=True,max_length=50)
    purpose_of_use=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    Duration_of_use=models.DateTimeField()
    number_of_times_day=models.IntegerField()
    type=models.CharField(max_length=100)
    expire_date=models.DateField(null=False,blank=True)
    def __str__(self):
        return self.DrugName
    class Meta:
        ordering=['DrugName']



class Reminder (models.Model):
    ReminderID=models.IntegerField(primary_key=True,null=False,blank=True)
    patientID=models.IntegerField(null=False,blank=True)
    DrugName=models.CharField(max_length=50,null=False,blank=True)
    StartDate=models.DateTimeField()
    EndDate=models.DateTimeField()
    State=models.BooleanField(null=False,blank=True)
    AlarmRecordes=models.TimeField()
    Notes=models.TextField(max_length=50)
    def __str__(self):
        return self.ReminderID
    class Meta:
        ordering=['ReminderID']



class Document(models.Model):
    DrugName=models.CharField(max_length=50)
    patientId=models.IntegerField()
    prescriptionID=models.CharField(max_length=50)
    exrays_test=models.ImageField(upload_to='photos%y%m%d')
    diseasesId=models.IntegerField()
    escortID=models.IntegerField()
