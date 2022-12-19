from django.shortcuts import render,redirect
from Candidate.models import Contact, Job, Application
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    job = Job.objects.all()[:3]
    # cjob = Job.objects.all().order_by('cname', '-itime')[:3]
    if request.user.is_authenticated :
        location = request.user.last_name
        
        ujob = Job.objects.all().filter(vname = location)[:3]
            
        return render(request, "index.html",{'job':job,'ujob':ujob})
        
    else :
        return render(request, "index.html",{'job':job})
        
     

def job(request):
    job = Job.objects.all()
    return render(request, "job.html",{'job':job})


def prejob(request):
    return render(request, "job.html")


def infojob(request):
    cname = request.GET.get("cname")
    job = Job.objects.all().filter(cname = cname)
    return render(request, "job-info.html",{'job':job})


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, "job.html")
    return render(request, "log-in.html")


def signuppage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        qualification = request.POST.get("qualification")
        password = request.POST.get("password")
        try :
           user =User.objects.create_user(username=username,email=email,last_name=qualification,password=password)
           login(request,user)
           return redirect("/")
        except  :
            messages.error(request,  "Username already exist !")
            return render(request, "sign-up.html",{'colour':'red'})
    return render(request, "sign-up.html")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(
            name=name, email=email, message=message, time=datetime.today()
        )
        contact.save()
        
        messages.success(request, "Your message has been sent !")
        return render(request, "contact-us.html",{'colour':'green'})
    return render(request, "contact-us.html")


def logoutpage(request):
    job = Job.objects.all()[:3]
    logout(request)
    messages.success(request, "Logged out !!!")
    return render(request, "index.html",{'colour':'red','job':job})

def aboutus(request):
    return render(request,"about-us.html")

def apply(request):
    if request.user.username=='':
        return render(request, "log-in.html")
    elif request.method == "GET":
        cname = request.GET.get("cname")
        vname = request.GET.get("vname")
        username = request.user.username
        email = request.user.email
        name = request.user.first_name
        qualification = request.user.last_name
        application = Application(
            company=cname, email=email, vacancy=vname, name=name, qualification=qualification,username=username
        )
        application.save()
        messages.success(request, "Your application has been sent !")
        return render(request, "index.html",{'colour':'green'}) 
    return render(request, "index.html")