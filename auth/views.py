from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from hackathon import settings
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        # auth=Authpage(request.POST)
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request,"user already exists")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"email already exists")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"user name must be under 10 charecter")
            return redirect('home')
        if len(password)<6:
            messages.error(request,"password can be more then 6 digits")
            return redirect('home')
 
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('app') 
    
    return render(request,"index.html")

def app(request):
    return render(request,"app.html")

def about(request):
    return render(request,"about.html")

def teacher(request):
    return render(request,"teacher.html")
def services(request):
    return render(request,"services.html")
def landing(request):
    return render(request,"landing.html")
def mlroad(request):
    return render(request,"ML_road.html")
def webroad(request):
    return render(request,"web_road.html")
def androad(request):
    return render(request,"android_road.html")

# def signup(request):
#     if request.method == 'POST':
#         # auth=Authpage(request.POST)
#         first_name=request.POST['fname']
#         last_name=request.POST['lname']
#         username=request.POST['user']
#         email=request.POST['email']
#         password=request.POST['password']
#         user_pass2=request.POST['password2']

#         if User.objects.filter(username=username):
#             messages.error(request,"user already exists")
#             return redirect('signup')
#         if User.objects.filter(email=email):
#             messages.error(request,"email already exists")
#             return redirect('signup')
#         if len(username)>10:
#             messages.error(request,"user name must be under 10 charecter")
#             return redirect('signup')
#         if len(password)<6:
#             messages.error(request,"password can be more then 6 digits")
#             return redirect('signup')
#         if user_pass2 !=password:
#             messages.error(request,"enter same password! ")
#             return redirect('signup')
#         if not username.isalnum():
#             messages.error(request,"user name must be alpha-numeric")
#             return redirect('home')
#         myuser=User.objects.create_user(username,email,password)
#         myuser.first_name=first_name
#         myuser.last_name=last_name
#         myuser.save()
#         messages.success(request,'thank you for register we sent you a mail')
#         #message part code 

#         subject="welcome to AI_core.com !!"
#         message="Hello "+ myuser.first_name + "!! \n" + "welcome to AI_core.com \n thank you for visiting our website \n we just sent yoou a conformation mail so that you can access our website by conform your mail and then activate your account \n thank you "+ myuser.first_name
#         from_mail=settings.EMAIL_HOST_USER
#         recipient_list=[myuser.email]
#         send_mail(subject,message,from_mail,recipient_list, fail_silently=True)

#         return redirect('signin')
#     return render(request,"signup.html")


def signin(request):
    if request.method == 'POST':
        user_name=request.POST['uname']
        user_pass=request.POST['password']
        user=authenticate(username=user_name,password=user_pass)
        print(user)
        if user is not None:
            login(request,user)
            fname=user.first_name
            messages.success(request,'congrates')
            return render(request,"app.html",{'fname':fname})
            # return render(request,"app.html",{'yname':yname})
        else:
            messages.error(request,'bad request')
            return redirect('signin')
    return render(request,"signin.html")


#def signout(request):
    #logout(request)
    # messages.success(request, "log out successfully")
    #return render(request, 'signin.html')
