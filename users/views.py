from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_register(request):
    if request.method == "POST":
        #Fetching Data
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']

        print("Method Type:",request.method)
        print("Username:",uname)
        print("Password:",upass)
        print("Confirm Password:",ucpass)
        print("Email:",uemail)

        # Validattion of data
        context={}
        if uname=="" or upass=="" or ucpass=="" or uemail=="":
            context['errmsg']="Field cannot be Blank"
            return render(request,"users/register.html",context)
        elif upass!=ucpass:
            context['errmsg']="Password and Confirm Password Mismatch"
            return render(request,"users/register.html",context)
        else:
            # u=User.objects.create(username=uname,password=upass,email=uemail,)
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save() #to store password in database
            context['success']='Account Created Successfully!! Please Login'
            
            #return HttpResponse("User Created Successfully")
            return render(request,'users/register.html',context)
    else:
        print("Method Type:",request.method)
        return render(request,'users/register.html')
    return HttpResponse("Shashikant")
    
def user_login(request):
    if request.method =="POST":
        #Fetching Data
        uname=request.POST['uname']
        upass=request.POST['upass']

        print('Method Type:',request.method)
        print('Username',uname)
        print('Password',upass)

        u=authenticate(username=uname,password=upass)
        # print("User Object:",u)
        # print("ID:",u.id)
        # print("Username:",u.username)
        # print("Password",u.password)
        # print("Email:",u.email)
        # print("SuperUser:",u.is_superuser)

        #retun HttpResponse("Details Fetched")

        if u is not None:
            login(request,u)
            return redirect('/food')
        else:
            context={}
            context['errmsg']="Invalid Username and Password"
            return render(request,'users/login.html',context)
            #retrun HttpResponse("Invalid Username and Password")
    
    else:
        print("Method Type:",request.method)
        return render(request,'users/login.html')
    

def user_logout(request):
    logout(request)
    return redirect('/users/login')
    