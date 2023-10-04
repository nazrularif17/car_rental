from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from .managers import UserManager
from datetime import timedelta

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USER_CHOICES = (
        ('admin', 'Admin'),
        ('car owner', 'Car owner'),
        ('car renter', 'Car renter'),
    )
    user_ID = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_CHOICES, default='car renter')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_ID'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user_ID
    
    @property
    def is_admin(self):
        return self.user_type == 'admin'

    @property
    def is_carrenter(self):
        return self.user_type == 'car renter'
    
    @property
    def is_carowner(self):
        return self.user_type == 'car owner'
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    AdminName=models.CharField(max_length=50)
    AdminPhonenum=models.CharField(max_length=12)
    AdminEmail=models.EmailField(max_length=255)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.AdminName
    
class CarRenter(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    LICENSE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    RentID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    RentName=models.CharField(max_length=50)
    RentPhonenum=models.CharField(max_length=12)
    RentEmail=models.EmailField(max_length=255)
    RentGender=models.CharField(max_length=6, choices=GENDER_CHOICES)
    RentLicense=models.CharField(max_length=3, choices=LICENSE_CHOICES)

    def __str__(self):
        return self.RentName
    
class CarOwner(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    OwnID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    OwnName=models.CharField(max_length=50)
    OwnPhonenum=models.CharField(max_length=12)
    OwnEmail=models.EmailField(max_length=255)
    OwnGender=models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.OwnName
    
class CarDetail(models.Model):
    CarPlatenum = models.CharField(primary_key=True, max_length=10)
    OwnID=models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    CarImg=models.ImageField(upload_to='images/car')
    CarModel = models.CharField(max_length=50)
    NumofPassenger = models.PositiveIntegerField()
    CarPrice = models.PositiveIntegerField()

    def __str__(self):
        return self.CarPlatenum
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    ]
    BookID = models.AutoField(primary_key=True)
    RentID = models.ForeignKey(CarRenter, on_delete=models.CASCADE)
    CarPlatenum = models.ForeignKey(CarDetail, on_delete=models.CASCADE)
    BookDate = models.DateField()
    ReturnDate = models.DateField()
    TotalPrice = models.PositiveIntegerField()
    BookStatus = models.CharField(max_length=7, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        duration = (self.ReturnDate - self.BookDate).days + 1
        self.TotalPrice = duration * self.CarPlatenum.CarPrice

        super().save(*args, **kwargs)
 
class Feedback(models.Model):
    FeedID = models.AutoField(primary_key=True)
    RentID=models.ForeignKey(CarRenter, on_delete=models.CASCADE)
    Comment = models.TextField(max_length=255)