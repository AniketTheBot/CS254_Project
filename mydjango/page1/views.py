from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
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

def review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        booktitle = request.POST.get('booktitle')
        review = request.POST.get('review')
    return render(request,'review.html')


def signin(request):
    return render(request,'signin.html')

def userdashboard(request):
    return render(request,'userdashboard.html')

def index(request):
    if request.method == "POST":
        booktitle = request.POST.get('booktitle')
        authorname = request.POST.get('authorname')
        ISBN = request.POST.get('ISBN')
        publdate = request.POST.get('publdate')
        desc = request.POST.get('desc')
    return render(request,'home.html')

