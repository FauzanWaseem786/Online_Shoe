from django.shortcuts import render,redirect
from django.conf import settings
import random
#from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
#from twilio.twiml.messaging_response import MessagingResponse
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from website_model.forms import Membr_form,ord_form,grp_form
from website_model.models import Member,ordr,Groop
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'website_model/home.html')
def reg(request):
    return render(request,'website_model/registered.html')
def Premium(request):
    return render(request,'website_model/premium.html')
def Variety(request):
    return render(request,'website_model/Variety.html')
def location(request):
    return render(request,'website_model/location.html')
def brands(request):
    return render(request,'website_model/brands.html')
def shoes (request):
    return render(request,'website_model/shoes.html')
def boots(request):
    return render(request,'website_model/boots.html')
def sandals(request):
    return render(request,'website_model/sandals.html')
def slippers(request):
    return render(request,'website_model/slippers.html')
def Membership(request):
    global registered
    global u1
    registered = False
    if(request.method == 'POST'):
        Member = Membr_form(request.POST,request.FILES)
        #profile = pro_form(request.POST,request.FILES)
        if Member.is_valid() :
            user = Member.save()
            username = request.POST.get('Name', '')
            u1=username
            password = request.POST.get('password', '')
            Email = request.POST.get('email', '')
            Hometown=request.POST.get('Hometown','')
            user.save()
            #profil = profile.save()
            #profil.save()
            user = authenticate(request, username=username, password=password,email=Email)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=username, password=password, email=Email)
                user.save()


        else:
            print("user_form.errors")
        return redirect('/otp/')
    else:
        Member=Membr_form()
        #profile=pro_form()
        return render(request,'website_model/premium.html',{ 'mem':Member,'registered':registered})
def login(request):
    logo=False
    if request.method == 'POST':
         username = request.POST.get('Name','')
         password = request.POST.get('password', '')

         user=authenticate(username=username,password=password)
         if user:
            if user.is_active:
                logi=True
                dj_login(request,user)
                #return HttpResponseRedirect(reverse('index'))

                return render(request,'website_model/home.html',{'logi':logi})
            else:
                return HttpResponse("Your account was inactive.")
         else:
            print("Someone tried to login and failed.")
            print("their credentials were username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'website_model/login.html', {})
@login_required
def ilogout(request):
    logout(request)
    return redirect('/login/')
def change(request):
    global Usr
    global n
    if(request.method == 'POST'):
        u=request.POST.get('Name','')
        Usr=User.objects.get(username=u)
        n=request.POST.get('newpassword','')

        return redirect('/pass_change_otp/')
    else:
        return render(request, 'website_model/chg_pswrd.html', {})
def pass_change_otp(request):
    global num
    if request.method == 'POST':
        otp=request.POST.get('otp','')
        if(int(otp)==int(num)):
            Usr.set_password(n)
            Usr.save()
            print(Usr,n)
            return redirect('/login/')
        else:
            return HttpResponse('Invalid OTP.')

    else:
        num=1000
        #no=random.randrange(1000,9999)
        #send_mail('Your OTP for verification',' Your OTP is {}'.format(no),'vasufauzan786@gmail.com',['vasufauzan1010@gmail.com'],fail_silently=False)
        return render(request, 'website_model/pass_otp.html', {})

def OrDer(request):
    if(request.method == 'POST'):
        O=True
        order =ord_form(request.POST)
        Email=request.POST.get('email_id','')
        if order.is_valid() :
            ord = order.save()
            ord.save()
            print('mail',Email)
            send_mail('Your order has been succesfully placed.','Thanks a lot for buying from us .','vasufauzan1010@gmail.com',[Email],fail_silently=False)
        else:
            print("user_form.errors")
    else:
        O=False
        order = ord_form()

    return render(request,'website_model/order.html',{ 'order':order,'O':O})

def broadcast_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)
global no
no=0
def otp(request):
    global no
    if request.method == 'POST':
        otp=request.POST.get('otp','')
        if(int(otp)==int(no)):
            return redirect('/reg/')
        else:
            u=Member.objects.filter(Name=u1)
            u.delete()
            us=User.objects.get(username=u1)
            us.delete()
            return HttpResponse('Invalid OTP.')

    else:
        no=1000
        #no=random.randrange(1000,9999)
        #send_mail('Your OTP for verification',' Your OTP is {}'.format(no),'vasufauzan786@gmail.com',['vasufauzan1010@gmail.com'],fail_silently=False)
        return render(request, 'website_model/otp.html', {})
def usraccnt(request):
    u2=request.GET.get('Name','')
    usr=Member.objects.all().filter(Name=u2)
    if(usr):
        usr=Member.objects.all().get(Name=u2)
        return render(request, 'website_model/User.html', {'user':usr})
    else:
        return HttpResponse('No such User, did you type the name correctly?')
def allusr(request):
    usrs=Member.objects.all()
    return render(request, 'website_model/users.html', {'usrs':usrs})
def crt_grp(request):
    if(request.method=='POST'):
        group = grp_form(request.POST,request.FILES)
        N=request.POST.get('Name','')
        nu=request.user
        m=Member.objects.get(Name=nu)
        if(group.is_valid()):
            group.save()
            g=Groop.objects.get(Name=N)
            g.Members.add(m)
        return render(request,'website_model/home.html',{})

    else:
        group=grp_form()
        return render(request,'website_model/create_group.html',{ 'grp':group })
@login_required
def grps(request,u_name='noone'):

    if(u_name!='noone'):
        g=Groop.objects.get(Name=u_name)
        nu=request.user
        m=Member.objects.get(Name=nu)
        if(m.Ingroup==True):
            g.Members.remove(m)
            Member.objects.filter(Name=nu).update(Ingroup=False)
        else:
            g.Members.add(m)
            Member.objects.filter(Name=nu).update(Ingroup=True)

        return redirect('/login/')
    else:
        grps=Groop.objects.all()
        nu=request.user
        m=Member.objects.get(Name=nu)
        f=m.Ingroup
        return render(request, 'website_model/groups.html', {'grps':grps,'f':f})
def dele_accnt(request):
    if(request.method=='POST'):
        a=request.user
        a.delete()
        m=Member.objects.get(Name=a)
        m.delete()
        return redirect('/login/')
    else:
        return render(request, 'website_model/del.html', {})
def edt(request,n="default"):
    global k
    if(request.method=='POST'):
        if(k!="default"):
            a=request.POST.get('Name','')
            b=request.POST.get('Hometown','')
            c=request.POST.get('Email','')
            m=Member.objects.get(Name=k)
            
            Member.objects.filter(Name=k).update(Name=a,HomeTown=b,Email=c)
            owner = User.objects.get (username=k)
            owner.username = a
            owner.save()
            return HttpResponse('Details updated succesfully.')
        else:
            print(n)
            return HttpResponse('please mention the details properly .')
    else:
        k=n
        return render(request, 'website_model/edt.html', {})
