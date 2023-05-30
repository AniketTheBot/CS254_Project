from django.shortcuts import render, HttpResponse

from page1.models import User,BookIssue,BookPublish,BookReview,Author


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def author(request):
    return render(request,'author.html')

def issuebooks(request):
    return render(request,'issuebooks.html')

def issuebooks(request):
    if request.method == "POST":
        booktitle = request.POST.get('booktitle')
        authorname = request.POST.get('authorname')
        ISBN = request.POST.get('ISBN')
    return render(request,'review')

def landing(request):
    return render(request,'landing.html')

def publishbook(request):
    return render(request,'publishbook.html')

def register(request):
    return render(request,'register.html')

def returnbook(request):
    return render(request,'returnbook.html')

def review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        booktitle = request.POST.get('booktitle')
        review = request.POST.get('review')

        rev = BookReview(username = name,booktitle = booktitle,review= review)
        rev.save()

        return HttpResponse("Review Added!")
    return render(request,'review.html')


def signin(request):
    return render(request,'signin.html')

def userdashboard(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User(username= username, password = password,email = email)
        user.save()
        
        return HttpResponse("User Info saved")
    return render(request,'userdashboard.html')


def publishbook(request):
    if request.method == "POST":
        booktitle = request.POST.get('booktitle')
        authorname = request.POST.get('authorname')
        ISBN = request.POST.get('ISBN')
        desc = request.POST.get('desc')
    return render(request,'home')

