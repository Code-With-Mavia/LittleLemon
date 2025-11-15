from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking, Menu
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.paginator import Paginator
import json

@login_required(login_url='/users/login/')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/users/login/')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/users/login/')
def contact(request):
    return render(request, 'contact.html')

@login_required
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(using='reservations')
    return render(request, 'book.html', {'form': form})

@csrf_exempt
@login_required
def bookings(request):
    if request.method == "POST":
        data = json.loads(request.body)
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
            return HttpResponse('{"error":1}', content_type='application/json')

    date = request.GET.get('date', str(datetime.today().date()))
    bookings_qs = Booking.objects.using('reservations').filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings_qs)
    return HttpResponse(booking_json, content_type='application/json')

@login_required
def menu(request):
    search_query = request.GET.get('search', '')
    menu_list = Menu.objects.filter(name__icontains=search_query) if search_query else Menu.objects.all()
    paginator = Paginator(menu_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'menu.html', {"menu_items": page_obj, "search_query": search_query})

@login_required
def display_menu_item(request, pk):
    try:
        menu_item = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})
