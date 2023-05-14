from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def author(request):
    return render(request,'author.html')

def issuebooks(request):
    return render(request,'issuebooks.html')

def landing(request):
    return render(request,'landing.html')

def publishbook(request):
    return render(request,'publishbook.html')

def register(request):
    return render(request,'register.html')

def returnbook(request):
    return render(request,'returnbook.html')

def review(request):
    return render(request,'review.html')

def signin(request):
    return render(request,'signin.html')

def userdashboard(request):
    return render(request,'userdashboard.html')

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
    return render(request,'home.html')

