from django.shortcuts import render,HttpResponse

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
    return HttpResponse("This is aboutpage !!")

def service(request):
    return HttpResponse("This is service page !!")



def contact(request):
    return HttpResponse("This is contact page !!")

def treatment(request):
    return HttpResponse("This is treatment page ...........!!")

def patato(request):
    return HttpResponse("patato treatment list  ...........!!")


