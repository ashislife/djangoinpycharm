from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # variable bhejne ka syntax
    context={
        'variable':"Es variable ko bhej jo jo maine banaya hai "
    }

    return render(request,'index.html',context)
    # return HttpResponse("This is Homepage !!")



# ye wahi req hai jo myapp ne bheji hai
def about(request):
    # return HttpResponse("This is aboutpage !!")
    return render(request,'about.html')


def service(request):
    # return HttpResponse("This is service page !!")
    return render(request, 'service.html')


# post request ko detabase me store kr do
def contact(request):
    # return HttpResponse("This is contact page !!")

    # database me add karne ka method
    if request.method=="POST":
        gmail=request.POST.get('gmail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact=Contact(gmail=gmail,subject=subject,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent")
    return render(request, 'contact.html')


def treatment(request):
    # return HttpResponse("This is treatment page ...........!!")
    return render(request, 'treatment.html')

def patato(request):
    # return HttpResponse("patato treatment list  ...........!!")
    return render(request, 'patato.html')

def tamato(request):
    return render(request, 'tamato.html')