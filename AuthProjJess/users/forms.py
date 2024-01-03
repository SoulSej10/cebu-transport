from typing import Any
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Request

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('Full_name', 'Email', 'Phone_Num', 'Birth_Date', 'Gender', 'AddressL1', 'AddressL2', 'Country', 'City', 'Region', 'Postal_Code')
        widgets = {
            'Full_name': forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter Full Name'}),
            'Email':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter Email Address'}),
            'Phone_Num':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter Phone number (xxxx xxx xxxx )'}),
            'Birth_Date':forms.DateInput(attrs={'class':'form-label','class':'form-control','placeholder':'Birth Date'}),
            'Gender':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Gender'}),
            'AddressL1':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Address Line 1'}),
            'AddressL2':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Address Line 2'}),
            'Country':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter your Country'}),
            'City':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter your City'}),
            'Region':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Enter your Region'}),
            'Postal_Code':forms.TextInput(attrs={'class':'form-label','class':'form-control','placeholder':'Postal Code (xxxx)'}),
        }
        


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email Account'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password'})



#------------------------------------------
from django import forms
from .models import BusTicket1

class BusTicketForm(forms.ModelForm):
    # Locations with coordinates
    locations = [
    'Alcoy',
    'Alumnos',
    'Anjo World',
    'Argao',
    'Ayala Center Cebu',
    'Banawa',
    'Basak',
    'Bulacao',
    'Carbon',
    'C Padilla',
    'Cebu CSBT',
    'Cebu Capitol',
    'Cebu IT Park',
    'Colon',
    'Dalaguete',
    'E Mall',
    'Fuente Osmeña Circle',
    'Guadalupe',
    'Il Corso',
    'Inayawan',
    'Jones',
    'Labangon',
    'Lahug',
    'Mabolo',
    'Mambaling Flyover',
    'Manalili',
    'Mantalongon, Dalaguete',
    'Panagdait',
    'Parkmall',
    'Pardo',
    'Pier',
    'Plaridel',
    'SM Seaside',
    'South Bus Terminal',
    'Talamban',
    'Urgello',
]
    # Bus types
    bus_types = [
        'Traditional jeep',
        'Modern jeep',
        'Ordinary City Bus',
        'Ordinary Provincial Bus',
        'Aircon City Bus',
        'Aircon Provincial Bus (Deluxe)',
        'Aircon Provincial Bus (Super deluxe)',
        'Aircon Provincial Bus Luxury',
    ]

    # Create a tuple of (location, location) for the dropdown choices
    location_choices = [(location, location) for location in locations]
    # Create a tuple of (bus_type, bus_type) for the dropdown choices
    bus_type_choices = [(bus_type, bus_type) for bus_type in bus_types]

    origin = forms.ChoiceField(choices=[('', 'Select Origin')] + location_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    destination = forms.ChoiceField(choices=[('', 'Select Destination')] + location_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    bus_type = forms.ChoiceField(choices=[('', 'Select Bus Type')] + bus_type_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))

    class Meta:
        model = BusTicket1
        fields = ['fullname', 'origin', 'destination', 'date', 'bus_type','qr_code']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'autofocus':'autofocus'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


# forms.py

from django import forms
from .models import BusTicket2

class BusTicketForm2(forms.ModelForm):
    locations = [
        # ... (your existing locations)
        'Alcoy',
    'Alumnos',
    'Anjo World',
    'Argao',
    'Ayala Center Cebu',
    'Banawa',
    'Basak',
    'Bulacao',
    'Carbon',
    'C Padilla',
    'Cebu CSBT',
    'Cebu Capitol',
    'Cebu IT Park',
    'Colon',
    'Dalaguete',
    'E Mall',
    'Fuente Osmeña Circle',
    'Guadalupe',
    'Il Corso',
    'Inayawan',
    'Jones',
    'Labangon',
    'Lahug',
    'Mabolo',
    'Mambaling Flyover',
    'Manalili',
    'Mantalongon, Dalaguete',
    'Panagdait',
    'Parkmall',
    'Pardo',
    'Pier',
    'Plaridel',
    'SM Seaside',
    'South Bus Terminal',
    'Talamban',
    'Urgello',
    ]

    bus_types = [
        # ... (your existing bus types)
        'Traditional jeep',
        'Modern jeep',
        'Ordinary City Bus',
        'Ordinary Provincial Bus',
        'Aircon City Bus',
        'Aircon Provincial Bus (Deluxe)',
        'Aircon Provincial Bus (Super deluxe)',
        'Aircon Provincial Bus Luxury',
    ]

    FULL_NAME_CHOICES = [
        ('student', 'Student (20% discount)'),
        ('senior_citizen', 'Senior Citizen'),
        ('voucher', 'Voucher'),
        ('regular', 'Regular'),
    ]

    location_choices = [(location, location) for location in locations]
    bus_type_choices = [(bus_type, bus_type) for bus_type in bus_types]

    origin = forms.ChoiceField(choices=[('', '-Select Origin-')] + location_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    destination = forms.ChoiceField(choices=[('', '-Select Destination-')] + location_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    bus_type = forms.ChoiceField(choices=[('', '-Select Bus Type-')] + bus_type_choices, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    discount = forms.ChoiceField(choices=[('', '-Select Discount-')] +FULL_NAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control custom-select selectpicker'}))
    
    class Meta:
        model = BusTicket2
        fields = ['fullname', 'origin', 'destination', 'date', 'bus_type', 'discount','qr_code']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'autofocus':'autofocus'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
