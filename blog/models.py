from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.bus_name

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'))
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return str(self.busid)
class feedback(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
# class seat_book(models.Model):
#     bus_id=models.ForeignKey(Book,on_delete=models.CASCADE)
#     BOOKED = 'B'
#     EMPTY = 'E'
#     seat_status = ((BOOKED, 'Booked'),
#                  (EMPTY, 'empty'))
#     seat_no1=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no2=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no3=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no4=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no5=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no6=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no7=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no8=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no9=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no10=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no11=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no12=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no13=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no14=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no15=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no16=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no17=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no18=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no19=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no20=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no21=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no22=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no22=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no23=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no24=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no24=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no25=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no26=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no27=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no28=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no29=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no30=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no31=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no32=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no33=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no34=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no35=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no36=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no37=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no38=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no39=models.CharField(choices=seat_status,default=EMPTY,max_length=2)
#     seat_no40=models.CharField(choices=seat_status,default=EMPTY,max_length=2)