from django.shortcuts import render

from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import  Bus, Book,feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import views
from django import forms
from django.contrib import messages


from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'blog/home.html')
    else:
        return redirect('login')
def about(request):
    return render(request,'blog/about.html')




@login_required
def findbus(request):
    context = {}
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')
        bus_list = Bus.objects.filter(source=source_r, dest=dest_r, date=date_r)
        if bus_list:
            return render(request, 'blog/list.html', locals())
        else:
            context["error"] = "Sorry no buses availiable"
            return render(request, 'blog/findbus.html', context)
    else:
        return render(request, 'blog/findbus.html')


@login_required
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Bus.objects.get(id=id_r)
        if bus:
            if  int(seats_r)>6:
                context["error"] = "please select a fewer number of seats not more than 6"
                return render(request, 'blog/findbus.html', context)

            elif bus.rem > int(seats_r):
                name_r = bus.bus_name
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.dest
                nos_r = Decimal(bus.nos)
                price_r = bus.price
                date_r = bus.date
                time_r = bus.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                book.save()
                return render(request, 'blog/bookings.html', locals())
            else:
                context["error"] = "we dont have those many of seats please select a fewer number of seats"
                return render(request, 'blog/findbus.html', context)

    else:
        return render(request, 'blog/findbus.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect('success')
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'blog/error.html', context)
    else:
        return render(request, 'blog/findbus.html')


@login_required
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'blog/booklist.html', locals())
    else:
        context['error'] = "Sorry no buses booked"
        return render(request, 'blog/findbus.html', context)
@login_required
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'blog/success.html', context)
@login_required(login_url='signin')
def page(request):
    context = {
        'posts': feedback.objects.all()
    }
    return render(request, 'blog/feedback.html', context)

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['content']

@login_required(login_url='signin')
def feedbackpage(request):
    if request.method == 'POST':
        comment=request.POST.get('content')
        
        
        u_form=feedback.objects.create(user_name=request.user,content=comment)
        u_form.save()          
        messages.success(request, f'Your account has been updated!')
        return redirect('page')  

    else:
        u_form = feedbackform(instance=request.user)
    context = {
        'form': u_form,
        
    }

    return render(request, 'blog/feedbac page.html', context)

# def bookseat(request):
#     seats_r = int(request.POST.get('no_seats'))
#     bus = Bus.objects.get(id=id_r)
#     if  int(seats_r)>6:
#                 context["error"] = "please select a fewer number of seats not more than 6"
#                 return render(request, 'blog/findbus.html', context)
#     elif bus.rem < int(seats_r):
#          context["error"] = "please select a fewer number of seats 6"
#          return render(request, 'blog/findbus.html', context)
    
    
#     elif request.method == 'POST':
#         bus = Book.objects.get(busid = request.POST.get('bus_id'))
#         seat_book.objects.filter(bus_id = bus)
#         for i in seat_book.objects.all() :
#             pass
#         seat = []
#         for i in range(40) :
#             seat.append("seat_no" + str(i)) 
            
#         print(seat)
#         context = {
#             'seats' : seat
#         }
#         return render(request,'blog/seats.html',context)

#     elif request.method == "GET" :
#         selected_seats = request.POST.getlist('selected_seats')
#         for i in selected_seats:
#             print(seat_book.objects.filter(bus_id=request.POST.get('bus_id')).update(status='BOOKED'))
#         return redirect('/seatbooking')
    
#     return render(request,'blog/seats.html')
#     elif request.method =="post"
    
    


    


