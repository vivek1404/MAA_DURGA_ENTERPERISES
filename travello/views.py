from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate 

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticated(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


    else:
        return render(request,'login.html')




def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'email taken')
                return redirect('register')

            else:

                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('password not matching..')
            messages.info(request,'password not matching..')
            return redirect('register')
        return redirect('/')

    else:
         return render(request,'register.html')





def index(request):

    dest1 = Destination()
    dest1.name = 'Delivery pipe'
    dest1.desc = 'It is pure and vigrin pipe'
    dest1.img = 'destination_1.jpg'
    dest1.price = 105

    dest2 = Destination()
    dest2.name = 'Delivery pipe'
    dest2.desc = 'It is pure and vigrin pipe'
    dest2.img = 'destination_2.jpg'
    dest2.price = 105

    dest3 = Destination()
    dest3.name = 'Delivery pipe'
    dest3.desc = 'It is pure and vigrin pipe'
    dest3.img = 'destination_3.jpg'
    dest3.price = 105

    dest4 = Destination()
    dest4.name = 'Delivery pipe'
    dest4.desc = 'It is pure and vigrin pipe'
    dest4.img = 'destination_4.jpg'
    dest4.price = 200

    dest5 = Destination()
    dest5.name = 'Delivery pipe'
    dest5.desc = 'It is pure and vigrin pipe'
    dest5.img = 'destination_5.jpg'
    dest5.price = 105

    dest6 = Destination()
    dest6.name = 'Delivery pipe'
    dest6.desc = 'It is pure and vigrin pipe'
    dest6.img = 'destination_6.jpg'
    dest6.price = 105

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]
    return render(request,'index.html', {'dests': dests})


def logout(request):
    auth.logout(request)
    return redirect('/')
