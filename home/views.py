from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    numbers={
        'fruits':['apple','banana','grapes']
    }
        
    
    


    # numbers={
    # 'num1':-10.9,
    # }

    # person={
    #     'name':'Kumar',
    #     'age':40,
    #     'place':'Calicut'
    # }
    # return HttpResponse("Home Page")
    return render(request,'index.html',numbers)

def about(request):
    # return HttpResponse("About Page")
    return render(request,'about.html')

def booking(request):
    # return HttpResponse("Booking page")
    return render(request,'booking.html')

def doctors(request):
    # return HttpResponse("Doctors Page")
    return render(request,'doctors.html')

def contact(request):
    # return HttpResponse("Contact Page")
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')