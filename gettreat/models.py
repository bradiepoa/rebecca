from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


    class Meta:
    	swappable = 'AUTH_USER_MODEL'


class Location(models.Model):

    STATUS_CHOICES =(
        ('available','Available'),
        ('none','None'),
        )

    Hospital_Loacation = models.CharField(max_length=200, blank=True, null=True)
    DateAdded = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, default='none', choices=STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.Hospital_Loacation

class Departments(models.Model):
    Department_Name = models.CharField(max_length=200, blank=True, null=True)
    DateAdded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Department_Name

class Hospital(models.Model):

    STATUS_CHOICES = (

        ('clinic','Clinic'),
        ('hospital','Hospital'),
        ('refferel','Refferel'),

        )

    Hospital_Name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, default='none', choices=STATUS_CHOICES, blank=True, null=True)
    Hospital_Loacation = models.ForeignKey(Location,on_delete=models.CASCADE, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Contact = models.CharField(max_length=200, blank=True, null=True)
    image  = models.ImageField()

    def __str__(self):
        return self.Hospital_Name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Hospital_Services(models.Model):
    Hospital_Name = models.ForeignKey(Hospital, on_delete=models.SET_NULL, blank=True, null=True)
    Departments = models.ForeignKey(Departments, on_delete=models.SET_NULL, blank=True, null=True)
    Service_Offered = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Service_Offered


class Our_Doctors(models.Model):
    STATUS_CHOICES = (
        ('permanent', 'Permanent'),
        ('temperory', 'Temperory'),
        ('not available', 'Not available'),
        )
    Hospital_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True,null=True)
    Doctors_Name = models.CharField(max_length=200, blank=True, null=True)
    Department_Name = models.ManyToManyField(Departments)
    Phone_Number = models.CharField(max_length=15, blank=True, null=True)
    Email = models.CharField(max_length=15, blank=True, null=True)
    Registered_Date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='temperory', blank=True, null=True)


    def __str__(self):
        return self.Doctors_Name

class Our_Patients(models.Model):
    STATUS_CHOICES = (
        ('on hold', 'On Hold'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),

        )
    GENDER_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        )

    patient_Name = models.CharField(max_length=200, blank=True, null=True)
    Date_Of_Birth = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default='female', blank=True, null=True)
    patient_id = models.CharField(max_length=2000, blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Address = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='on hold', blank=True, null=True)
    image = models.ImageField(upload_to='patients')
    DateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_Name


    @property
    def imageURL(self):
        try:
            url = self.image.url

        except:
            url = ''
        return url

   

class Appointments(models.Model):

    APPOIT_CHOICE = (

        ('accepted', 'Accepted'),
        ('pending', 'Pending'),
        ('declined', 'Declined'),
        )

    Hospital_Name = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    patient_Name = models.CharField(max_length=200, blank=True, null=True)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    patient_id = models.CharField(max_length=2000, blank=True, null=True)

    Description = models.TextField(blank=True, null=True)

    Immediete_phone = models.CharField(max_length=200, blank=True, null=True)

    status = models.CharField(max_length=200, choices=APPOIT_CHOICE, default='pending', blank=True, null=True)

    AddedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient_Name


class Disease(models.Model):

    Name = models.CharField(max_length=200, blank=True)

    Description = models.TextField(blank=True, null=True)

    AddedDate = models.DateTimeField(auto_now_add=True,)


class Medication(models.Model):

    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    patient_Name = models.CharField(max_length=200, blank=True, null=True)

    Added_Date = models.DateField(auto_now_add=True)

class Bills(models.Model):

    STATUS_CHOICES= (

        ('pending', 'Pending'),
        ('cleared', 'Cleared'),

        )

    patient_Name = models.CharField(max_length=200, blank=True, null=True)

    patient_id = models.CharField(max_length=200, blank=True, null=True)

    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending', blank=True, null=True)

    Paid_Date = models.DateTimeField(auto_now_add=True,)

class Emergency(models.Model):

    STATUS_CHOICES = (

        ('declined', 'Declined'),
        ('pending', 'Pending'),
        ('picked', 'Picked'),
        ('admitted', 'Admitted'),

        )


    patient_Name = models.CharField(max_length=200, blank=True, null=True)

    Phone_Number = models.CharField(max_length=15, blank=True, null=True)

    patient_id = models.CharField(max_length=100, blank=True, null=True)

    Hospital = models.CharField(max_length=200, blank=True, null=True)

    Location_Discription = models.TextField(blank=True, null=True)

    Request_Date = models.DateTimeField(auto_now_add=True, blank=True)

    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending',blank=True)

    def __str__(self):
        return self.Request_Date










   



