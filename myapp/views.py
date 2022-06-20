from django.shortcuts import redirect, render
from .forms import usersignupForm,notesForm
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings


# Create your views here.

def appLogin(request):
    unm=request.POST['username']
    pas=request.POST['password']
    print("Username:",unm)
    print("Password:",pas)
    user=userSignup.objects.filter(username=unm,password=pas)
    userid=userSignup.objects.get(username=unm)
    #print("UserID:",userid.id)
    if user:
        print("Login Successfully!")
        request.session['user']=unm
        request.session['userid']=userid.id
    else:
        print("Error...Login fail!")

def appSignup(request):
    newuser=usersignupForm(request.POST)
    if newuser.is_valid():
        newuser.save()
        print("Signup Successfully!")
    else:
        print(newuser.errors)

def index(request):
    user=request.session.get('user') #fetch session data
    if request.method=='POST': # root
        if request.POST.get('signup')=='signup': #child
            appSignup(request)

            #Send Mail Code
            sub="Welcome!"
            msg=f"Hello User, \nYour account has been created with us!\n\nEjoy our services.\n\nThanks & Regards!\nSanket Chauhan\nTOPS Technologies\n+91 9724799469 | sanket@tops-int.com"
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=["pandyanirav15@gmail.com","ramanidhaval11@gmail.com","amitadhandha301990@gmail.com","unadkatdhara9@gmail.com"]
            to_ID=[request.POST['username']]

            send_mail(sub,msg,from_ID,to_ID)

            return redirect('notes')
        elif request.POST.get('login')=='login': # child
            appLogin(request)
            return redirect('notes')
    return render(request,'index.html',{'user':user})

def notes(request):
    user=request.session.get('user') #fetch session data
    if request.method=='POST':
        mynotes=notesForm(request.POST,request.FILES)
        if mynotes.is_valid():
            mynotes.save()
            print("Your post has been updated!")
            return redirect('notes')
        else:
            print(mynotes.errors)
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user') #fetch session data
    userid=request.session.get('userid') #fetch userid
    uid=userSignup.objects.get(id=userid)
    if request.method=='POST':
        updatefrm=usersignupForm(request.POST)
        if updatefrm.is_valid():
            updatefrm=usersignupForm(request.POST,instance=uid)
            updatefrm.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updatefrm.errors)
    return render(request,'profile.html',{'user':user,'userid':userSignup.objects.get(id=userid)})

def about(request):
    user=request.session.get('user') #fetch session data
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user') #fetch session data
    return render(request,'contact.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')