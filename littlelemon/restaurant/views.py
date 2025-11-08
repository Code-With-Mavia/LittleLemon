from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
from django.core.paginator import Paginator
from .forms import BookingForm
from .models import Booking, Menu


# ------------------------
# Standard page views
# ------------------------
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# ------------------------
# Booking form view
# ------------------------
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save booking to reservations DB
            form.save(using='reservations')
    return render(request, 'book.html', {'form': form})


# ------------------------
# Bookings API view
# ------------------------
@csrf_exempt
def bookings(request):
    if request.method == "POST":
        # Load JSON data from request body
        data = json.loads(request.body)

        # Check if the reservation slot is already taken
        exists = Booking.objects.using('reservations').filter(
            reservation_date=data['reservation_date'],
            reservation_slot=data['reservation_slot']
        ).exists()

        if not exists:
            booking = Booking(
                first_name=data['first_name'],
                last_name=data.get('last_name', ''),
                guest_number=data.get('guest_number', 1),
                comment=data.get('comment', ''),
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot']
            )
            booking.save(using='reservations')
        else:
            return HttpResponse(
                '{"error":1}',
                content_type='application/json'
            )

    # Handle GET request: return bookings for a given date
    date = request.GET.get('date', str(datetime.today().date()))
    bookings_qs = Booking.objects.using('reservations').filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings_qs)
    return HttpResponse(booking_json, content_type='application/json')


# ------------------------
# Menu views
# ------------------------
def menu(request):
    search_query = request.GET.get('search', '')
    if search_query:
        menu_list = Menu.objects.filter(name__icontains=search_query)
    else:
        menu_list = Menu.objects.all()
    
    paginator = Paginator(menu_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'menu.html', {"menu_items": page_obj, "search_query": search_query})


def display_menu_item(request, pk):
    try:
        menu_item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})