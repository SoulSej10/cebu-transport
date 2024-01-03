from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Request
from .forms import RequestForm

from django.core.files.base import ContentFile
import os
import qrcode

# Create your views here.
@login_required(login_url='login_reg')
def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='login_reg')
def billing(request):
    return render(request, 'users/billing.html')

@login_required(login_url='login_reg')
def about(request):
    return render(request, 'users/about.html')

@login_required(login_url='login_reg')
def explore(request):
    return render(request, 'users/explore.html')

def Log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username , password=password)
        print('USER', user)
        if user is not None:
            login(request, user)
            return redirect ('home')

    return render(request, 'users/Log.html')

def memereq(request):
    submitted = False
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/memereq?submitted=True')
    else:
        form = RequestForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'users/memereq.html', {'form': form, 'submitted': submitted})

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        user = authenticate(request, username=username, email=email, password=password, password2=password2)
        
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'users/Register.html')

def login_reg(request):
    page ='login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print('USER: ', user)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.success(request, ("Incorrect Input! Try Again"))
            return redirect ('login_reg')
    else:  
        return render(request, 'users/sample_log.html', {'page': page})

def log_out(request):
    logout(request)
    return redirect('login_reg')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('login_reg')

    context = {'form': form, 'page' : page }
    return render (request, 'users/sample_log.html', context)

def all_Request(request):
    Request_list = Request.objects.all()
   # return redirect('home')
    return render(request, 'users/request_event.html', {'Request_list': Request_list})



def home(request):
    form = BusTicketForm()
    return render(request, 'users/home.html', {'form': form})

#-----------------------------------
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from geopy.distance import geodesic
from .forms import BusTicketForm
from .models import BusTicket1, BusTicket2

def calculate_fee(distance, bus_type):
    # Bus type information
    bus_types = {
        'Traditional jeep': {'min_fare': 12, 'after_4km': 1.80, 'after_5km': 2.15},
        'Modern jeep': {'min_fare': 14, 'after_4km': 2.20, 'after_5km': 2.20},
        'Ordinary City Bus': {'min_fare': 13, 'after_4km': 2.20, 'after_5km': 2.25},
        'Ordinary Provincial Bus': {'min_fare': 13, 'after_4km': 2.15, 'after_5km': 1.90},
        'Aircon City Bus': {'min_fare': 15, 'after_4km': 2.25, 'after_5km': 2.14},
        'Aircon Provincial Bus (Deluxe)': {'min_fare': 15, 'after_4km': 2.45, 'after_5km': 2.10},
        'Aircon Provincial Bus (Super deluxe)': {'min_fare': 16, 'after_4km': 2.50, 'after_5km': 2.35},
        'Aircon Provincial Bus Luxury': {'min_fare': 16, 'after_4km': 2.50, 'after_5km': 2.90},
    }

    # Get bus type details
    bus_type_details = bus_types.get(bus_type, {})

    if not bus_type_details:
        return None  # Handle invalid bus type

    # Example fee calculation, adjust based on your business rules
    min_fare = bus_type_details.get('min_fare', 0)
    after_4km = bus_type_details.get('after_4km', 0)
    after_5km = bus_type_details.get('after_5km', 0)

    if distance <= 4:
        fee = min_fare
    elif distance <= 5 and after_5km is not None:
        fee = after_5km
    else:
        fee = min_fare + (distance - 4) * after_4km

    return fee

def calculate_distance_and_fee(origin, destination, bus_type):
    # Replace this with the actual implementation using geopy's geodesic function
    # You should implement getting coordinates from location names using geopy
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)

    # Calculate distance
    distance = geodesic(origin_coords, destination_coords).kilometers

    # Calculate fee based on distance and bus type
    fee = calculate_fee(distance, bus_type)

    return distance, fee

def generate_qr_code(ticket_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Ticket ID: {ticket_id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code as an image file
    img_filename = f"bus_ticket_qrcode_{ticket_id}.png"
    img_path = os.path.join('media', 'qrcodes', img_filename)
    img.save(img_path)

    return img_path

def bus_ticket(request):
    if request.method == 'POST':
        form = BusTicketForm(request.POST)
        if form.is_valid():
            bus_ticket = form.save(commit=False)
            
            # Calculate distance and fee
            bus_ticket.distance, bus_ticket.total_fee = calculate_distance_and_fee(bus_ticket.origin, bus_ticket.destination, bus_ticket.bus_type)
            bus_ticket.distance = round(bus_ticket.distance, 2)
            bus_ticket.total_fee = round(bus_ticket.total_fee, 2)
            bus_ticket.save()

            # Generate QR code and save the path in the BusTicket1 instance
            qr_code_path = generate_qr_code(bus_ticket.id)
            bus_ticket.qr_code.save(os.path.basename(qr_code_path), ContentFile(open(qr_code_path, "rb").read()))

            # Use render instead of HttpResponse
            return render(request, 'users/bus_ticket.html', {'bus_ticket': bus_ticket})
    else:
        form = BusTicketForm()

    return render(request, 'users/bus_ticket.html', {'form': form})

# Placeholder function, replace with actual implementation
def get_coordinates(location_name):
    # Implement a function to get coordinates from the location name
    # Use the provided data for location coordinates
    location_coordinates = {
        'Alcoy': (9.9373, 123.4414),
        'Alumnos': (10.3077, 123.9177),
        'Anjo World': (10.2359, 123.9933),
        'Argao': (9.8772, 123.6093),
        'Ayala Center Cebu': (10.3173, 123.9054),
        'Banawa': (10.3034, 123.8848),
        'Basak': (10.2803, 123.8704),
        'Bulacao': (10.2818, 123.8358),
        'Carbon': (10.2913, 123.9070),
        'C Padilla': (10.2795, 123.8881),
        'Cebu CSBT': (10.3157, 123.8854),
        'Cebu Capitol': (10.3157, 123.8854),
        'Cebu IT Park': (10.3182, 123.9055),
        'Colon': (10.2923, 123.9051),
        'Dalaguete': (9.7617, 123.5345),
        'E Mall': (10.2893, 123.8665),
        'Fuente Osmeña Circle': (10.3162, 123.9005),
        'Guadalupe': (10.3036, 123.8931),
        'Il Corso': (10.2715, 123.9338),
        'Inayawan': (10.2673, 123.8696),
        'Jones': (10.2961, 123.9024),
        'Labangon': (10.2959, 123.8799),
        'Lahug': (10.3436, 123.9147),
        'Mabolo': (10.3234, 123.9161),
        'Mambaling Flyover': (10.2808, 123.8743),
        'Manalili': (10.2930, 123.9042),
        'Mantalongon, Dalaguete': (9.7521, 123.5728),
        'Panagdait': (10.3178, 123.9057),
        'Parkmall': (10.3487, 123.9182),
        'Pardo': (10.2755, 123.8702),
        'Pier': (10.2927, 123.9032),
        'Plaridel': (10.3145, 123.9216),
        'SM Seaside': (10.2693, 123.9044),
        'South Bus Terminal': (10.2884, 123.8656),
        'Talamban': (10.3552, 123.9139),
        'Urgello': (10.3129, 123.8905),
        # Add coordinates for other locations
    }

    return location_coordinates.get(location_name, (0.0, 0.0))  # Default to (0.0, 0.0) if not found


# views.py

from django.shortcuts import render
from django.http import HttpResponse
from geopy.distance import geodesic
from .forms import BusTicketForm2
from .models import BusTicket2

def billing(request):
    form = BusTicketForm2()
    return render(request, 'users/billing.html', {'form': form})
# ... (your existing code)
def calculate_fee(distance, bus_type):  
    # Bus type information
    bus_types = {
        'Traditional jeep': {'min_fare': 40, 'after_4km': 1.80, 'after_5km': 2.15},
        'Modern jeep': {'min_fare': 40, 'after_4km': 2.20, 'after_5km': 2.20},
        'Ordinary City Bus': {'min_fare': 50, 'after_4km': 2.20, 'after_5km': 2.25},
        'Ordinary Provincial Bus': {'min_fare': 50, 'after_4km': 2.15, 'after_5km': 1.90},
        'Aircon City Bus': {'min_fare': 50, 'after_4km': 2.25, 'after_5km': 2.14},
        'Aircon Provincial Bus (Deluxe)': {'min_fare': 55, 'after_4km': 2.45, 'after_5km': 2.10},
        'Aircon Provincial Bus (Super deluxe)': {'min_fare': 55, 'after_4km': 2.50, 'after_5km': 2.35},
        'Aircon Provincial Bus Luxury': {'min_fare': 55, 'after_4km': 2.50, 'after_5km': 2.90},
    }

    # Get bus type details
    bus_type_details = bus_types.get(bus_type, {})

    if not bus_type_details:
        return None  # Handle invalid bus type

    # Example fee calculation, adjust based on your business rules
    min_fare = bus_type_details.get('min_fare', 0)
    after_4km = bus_type_details.get('after_4km', 0)
    after_5km = bus_type_details.get('after_5km', 0)

    if distance <= 4:
        fee = min_fare
    elif distance <= 5 and after_5km is not None:
        fee = after_5km
    else:
        fee = min_fare + (distance - 4) * after_4km

    return fee

def calculate_distance_and_fee(origin, destination, bus_type):
    # Replace this with the actual implementation using geopy's geodesic function
    # You should implement getting coordinates from location names using geopy
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)

    # Calculate distance
    distance = geodesic(origin_coords, destination_coords).kilometers

    # Calculate fee based on distance and bus type
    fee = calculate_fee(distance, bus_type)

    return distance, fee

def get_coordinates(location_name):
    # Implement a function to get coordinates from the location name
    # Use the provided data for location coordinates
    location_coordinates = {
        'Alcoy': (9.9373, 123.4414),
        'Alumnos': (10.3077, 123.9177),
        'Anjo World': (10.2359, 123.9933),
        'Argao': (9.8772, 123.6093),
        'Ayala Center Cebu': (10.3173, 123.9054),
        'Banawa': (10.3034, 123.8848),
        'Basak': (10.2803, 123.8704),
        'Bulacao': (10.2818, 123.8358),
        'Carbon': (10.2913, 123.9070),
        'C Padilla': (10.2795, 123.8881),
        'Cebu CSBT': (10.3157, 123.8854),
        'Cebu Capitol': (10.3157, 123.8854),
        'Cebu IT Park': (10.3182, 123.9055),
        'Colon': (10.2923, 123.9051),
        'Dalaguete': (9.7617, 123.5345),
        'E Mall': (10.2893, 123.8665),
        'Fuente Osmeña Circle': (10.3162, 123.9005),
        'Guadalupe': (10.3036, 123.8931),
        'Il Corso': (10.2715, 123.9338),
        'Inayawan': (10.2673, 123.8696),
        'Jones': (10.2961, 123.9024),
        'Labangon': (10.2959, 123.8799),
        'Lahug': (10.3436, 123.9147),
        'Mabolo': (10.3234, 123.9161),
        'Mambaling Flyover': (10.2808, 123.8743),
        'Manalili': (10.2930, 123.9042),
        'Mantalongon, Dalaguete': (9.7521, 123.5728),
        'Panagdait': (10.3178, 123.9057),
        'Parkmall': (10.3487, 123.9182),
        'Pardo': (10.2755, 123.8702),
        'Pier': (10.2927, 123.9032),
        'Plaridel': (10.3145, 123.9216),
        'SM Seaside': (10.2693, 123.9044),
        'South Bus Terminal': (10.2884, 123.8656),
        'Talamban': (10.3552, 123.9139),
        'Urgello': (10.3129, 123.8905),
        # Add coordinates for other locations
    }

    return location_coordinates.get(location_name, (0.0, 0.0))  # Default to (0.0, 0.0) if not found
def calculate_discounted_fare(initial_fare, discount):
    # Implement your logic to calculate discounted fare based on the discount type
    if discount == 'student':
        return initial_fare * 0.8  # 20% discount for students
    elif discount == 'senior_citizen':
        return initial_fare * 0.85  # 15% discount for senior citizens
    elif discount == 'voucher':
        return initial_fare * 0.9  # 10% discount for voucher
    else:
        return initial_fare  # No discount

def generate_qr_code(ticket_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Ticket ID: {ticket_id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code as an image file
    img_filename = f"bus_ticket_qrcode_{ticket_id}.png"
    img_path = os.path.join('media', 'qrcodes', img_filename)
    img.save(img_path)

    return img_path

def bus_ticket_signed_up(request):
    if request.method == 'POST':
        form = BusTicketForm2(request.POST)
        if form.is_valid():
            bus_ticket = form.save(commit=False)

            # Calculate distance and fee
            bus_ticket.distance, bus_ticket.initial_fare = calculate_distance_and_fee(bus_ticket.origin, bus_ticket.destination, bus_ticket.bus_type)
            bus_ticket.distance = round(bus_ticket.distance, 2)
            bus_ticket.initial_fare = round(bus_ticket.initial_fare, 2)

            # Calculate discounted fare
            bus_ticket.total_fare = calculate_discounted_fare(bus_ticket.initial_fare, bus_ticket.discount)
            bus_ticket.total_fare = round(bus_ticket.total_fare, 2)

            bus_ticket.save()

            # Generate QR code and save the path in the BusTicket2 instance
            qr_code_path = generate_qr_code(bus_ticket.id)
            bus_ticket.qr_code.save(os.path.basename(qr_code_path), ContentFile(open(qr_code_path, "rb").read()))

            return render(request, 'users/bus_ticket_signed_up.html', {'bus_ticket': bus_ticket})
    else:
        form = BusTicketForm2()

    return render(request, 'users/bus_ticket_signed_up.html', {'form': form})