import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

# Create your models here.

class Request(models.Model):
    Full_name = models.CharField('User Name', max_length=120)
    Email = models.EmailField('Email')
    Phone_Num = models.CharField('Phone Number',max_length=40)
    Birth_Date = models.DateTimeField('BirthDate')
    Gender = models.CharField('Gender',max_length=30, blank=True)
    AddressL1 = models.CharField('Address Line 1', max_length=120)                                  
    AddressL2 =models.CharField('Address Line 2', max_length=120)
    Country = models.CharField('Country',max_length=120)
    City = models.CharField('City', max_length=120)
    Region = models.CharField('Region', max_length=120)
    Postal_Code = models.CharField('Postal Code', max_length=20)

#------------------------------------------------------------------
# models.py
from django.db import models

class BusTicket1(models.Model):
    fullname = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    distance = models.FloatField(null=True, blank=True)
    total_fee = models.FloatField(null=True, blank=True)
    bus_type = models.CharField(max_length=100)

    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate and save the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.get_ticket_info())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer)
        self.qr_code.save(f"qrcodes/{self.fullname}_qrcode.png", File(buffer), save=False)

        super().save(*args, **kwargs)

    def get_ticket_info(self):
        # Customize this method to return the information you want in the QR code
        return f"BUS TICKET INFORMATION SUMMARY\n\nPassenger Name: {self.fullname}\nOrigin: {self.origin}\nDestination: {self.destination}\nDate of Purchase: {self.date}\nBus Transport Type: {self.bus_type}\nTotal Fee: {self.total_fee} \nPayment Method: GCASH ONLY \n\nThank you for choosing CEBU TRANSPORT! \nAsk us anytime..."

    def __str__(self):
        return self.fullname


# models.py

from django.db import models

class BusTicket2(models.Model):
    FULL_NAME_CHOICES = [
        ('student', 'Student (20% discount)'),
        ('senior_citizen', 'Senior Citizen'),
        ('voucher', 'Voucher'),
        ('regular', 'Regular'),
    ]

    fullname = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    distance = models.FloatField(null=True, blank=True)
    initial_fare = models.FloatField(null=True, blank=True)
    discount = models.CharField(max_length=15, choices=FULL_NAME_CHOICES, default='none')
    total_fare = models.FloatField(null=True, blank=True)
    bus_type = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50, default='gcash')

    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate and save the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.get_ticket_info())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer)
        self.qr_code.save(f"qrcodes/{self.fullname}_qrcode.png", File(buffer), save=False)

        super().save(*args, **kwargs)

    def get_ticket_info(self):
        # Customize this method to return the information you want in the QR code
        return f"BUS TICKET INFORMATION SUMMARY\n\nPassenger Name: {self.fullname}\nOrigin: {self.origin}\nDestination: {self.destination}\nTotal Distance: {self.distance}km\nDate of Purchase: {self.date}\nBus Transport Type: {self.bus_type}\nInitial Fee: {self.initial_fare}\nDiscount: {self.discount}\nTotal Fee: {self.total_fare}\nPayment Method: GCASH ONLY \n\nThank you for choosing CEBU TRANSPORT! \nAsk us anytime..."

    def __str__(self):
        return self.fullname
