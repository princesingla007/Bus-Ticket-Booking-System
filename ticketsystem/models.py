from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_name=models.CharField(max_length=55,default="")
    bus_start=models.CharField(max_length=55,default="")
    destination=models.CharField(max_length=55,null=False,default="")
    seats=models.IntegerField(default=1)
    available_seats=models.IntegerField()
    departure_time=models.DateTimeField()
    price=models.IntegerField(default=0)
    bus_number=models.CharField(max_length=50,null=False,default="")

    def __str__(self):
        return self.bus_name
    
class Booking(models.Model):
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    passenger_name=models.CharField(max_length=50)
    seats_booked = models.IntegerField(default=1)
    booked_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.bus.bus_name}"
