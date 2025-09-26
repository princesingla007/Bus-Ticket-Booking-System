from django.shortcuts import render,get_object_or_404
from .models import Bus,Booking
from django.http import HttpResponse

# Create your views here.

def index(request):
    buses=[]
    if request.method=="POST":
        bus_start=request.POST.get("bus_start")
        destination=request.POST.get("destination")
        buses=Bus.objects.filter(bus_start__icontains=bus_start,destination__icontains=destination)
    return render(request,"index.html",{"buses":buses})

def base(request):
    return render(request,"base.html")

def bus_list(request):
    bus=Bus.objects.all()
    return render(request,"bus_list.html",{"bus":bus})

def bus_book(request,id):
    bus=get_object_or_404(Bus,id=id)
    if request.method=="POST":
        passenger_name=request.POST.get("passenger_name")
        seats_booked=int(request.POST.get("seats_booked",1))
        
        if seats_booked <= 0:
            return HttpResponse("Invalid number of seats!")

        if bus.available_seats >= seats_booked:
            total_price=seats_booked*bus.price
            Booking.objects.create(bus=bus,passenger_name=passenger_name,seats_booked=seats_booked)
            bus.available_seats -=seats_booked
            bus.save()
            return render(request,"success.html",{"bus":bus,"passenger_name":passenger_name,"seats_booked":seats_booked,"total_price":total_price})
        else:
            return HttpResponse(f"Only {bus.available_seats} Seats left")
        
    return render(request, "bus_book.html", {"bus": bus})   


def success(request):
    return render(request,"sucsess.html")

def about(request):
    return render(request,"about.html")
            

