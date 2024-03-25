from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Departments,Doctors

# Create your views here.
def index(request):
   
    return render(request,'index.html')

def about(request):
    # return HttpResponse("About Page")
    return render(request,'about.html')

def booking(request):
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    # return HttpResponse("Doctors Page")
    return render(request,'doctors.html',dict_docs)

def contact(request):
    # return HttpResponse("Contact Page")
    return render(request,'contact.html')

def department(request):
    dict_dept={
       'dept' :Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)