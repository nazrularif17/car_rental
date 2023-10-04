from .models import Admin, User, CarRenter, CarOwner, CarDetail, Booking
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    class Meta:
        model = User
        fields = ('user_ID', 'password1', 'password2')
        widgets = {
            'user_ID': forms.TextInput(attrs={'placeholder': 'ID'}),
        }

class CarRenterForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    LICENSE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    RentGender = forms.ChoiceField(widget=forms.RadioSelect , choices=GENDER_CHOICES)
    RentLicense = forms.ChoiceField(widget=forms.RadioSelect, choices=LICENSE_CHOICES)
      
    class Meta:
        model = CarRenter
        fields = ['RentName', 'RentPhonenum', 'RentEmail', 'RentGender', 'RentLicense']
        widgets = {
            'RentName': forms.TextInput(attrs={'placeholder': 'Name'}),
            'RentPhonenum': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
            'RentEmail': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

class CarOwnerForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    OwnGender = forms.ChoiceField(widget=forms.RadioSelect , choices=GENDER_CHOICES)
      
    class Meta:
        model = CarOwner
        fields = ['OwnName', 'OwnPhonenum', 'OwnEmail', 'OwnGender']
        widgets = {
            'OwnName': forms.TextInput(attrs={'placeholder': 'Name'}),
            'OwnPhonenum': forms.NumberInput(attrs={'placeholder': 'Phone Number'}),
            'OwnEmail': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

class CarDetailForm(forms.ModelForm):
    
    class Meta:
        model = CarDetail
        fields = ["CarPlatenum","OwnID","CarImg","CarModel","NumofPassenger","CarPrice"]

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ["RentID","CarPlatenum","BookDate","ReturnDate"]

class OwnerAddCarForm(forms.ModelForm):
    
    class Meta:
        model = CarDetail
        fields = ["CarPlatenum","CarImg","CarModel","NumofPassenger","CarPrice"]

class RenterBookingForm(forms.ModelForm):
   
    class Meta:
        model = Booking
        fields = ["CarPlatenum","BookDate","ReturnDate"]
        widgets = {
            'BookDate': forms.DateInput(attrs={'type':'date'}),
            'ReturnDate': forms.DateInput(attrs={'type':'date'})
        }