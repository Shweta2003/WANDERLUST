from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db import connection
from.models import comment

# Create your views here
def comments(request):
    cursor=connection.cursor()
    cursor.execute('''select id from accounts_comment''')
    d=cursor.fetchall()
    for i in d:
        a=i[0]
    if request.method=='POST':
        a+=1
        name=request.POST.get('name','guest')
        post=request.POST.get('post','nothing')

        cursor.execute('''insert into accounts_comment values ({0},'{1}','{2}')'''.format(a,name,post))
        co=comment.objects.all()

        return render(request,'come.html',{'co':co})

def search(request):
    if request.method=='POST':
        place=request.POST.get('place','guest')
        cursor=connection.cursor()
        cursor.execute('''select name from travello_Destination''')
        fool=cursor.fetchall()
        print(fool)
        for i in fool:
            for j in i:
                if j==place:
                    print('yes')
                    return redirect('/hotels/%s'%(place[:6]))
        else:
            messages.info(request,"This place is not registered in our site yet.... comment below to add it!!")
            return redirect('/')
    else:
        return redirect('/')
def home(request):
    if request.method=='POST':
        return redirect("/")

def contact(request):
    if request.method=='GET':
        return render(request,'contact.html')
    elif request.method=='POST':
        return redirect('/')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials!!!!')
            return redirect('login')
    else:
        return render(request, 'login.html')



def Register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'SORRY USERNAME TAKEN.....Try taking another username')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'SORRY EMAIL TAKEN....Try using another email ID')
                return redirect('Register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save;
                print("User created successfully")
                return redirect('login')

        else:
            messages.info(request,'PASSWORD NOT MATCHING... please enter the same password for confirmation')
            return redirect('Register')

        return redirect('/')
    else:
        return render(request,'Register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def book(request):
    if request.method == "GET":
        return render(request,'book.html')

def pay(request):
    cursor = connection.cursor()
    cursor.execute('''select id from accounts_book''')
    d = cursor.fetchall()
    a=0
    for i in d:
        for j in i:
            a = j
    if request.method=='POST':
        a+=2
        first_name=request.POST.get('first_name','shweta')
        last_name=request.POST.get('last_name','Mandal')
        account=request.POST.get('account','100 100 100')
        password=request.POST.get('password','nothing')
        email=request.POST.get('email','sss@gmail.com')
        cursor.execute('''insert into accounts_book values({0},'{1}','{2}','{3}','{4}','{5}')'''.format(a,first_name,last_name,account,password,email))
        return redirect('/accounts/sorry')
    else:
        return render(request,'account.html')

def sorry(request):
    return render(request,'sorry.html')
