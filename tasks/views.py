from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')


def regis(request):
    
    if request.method == 'GET':
        return render(request, 'regis.html', {
        'form' : UserCreationForm
        })
    else: #si el reques metodo es post
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                   username=request.POST['username'],
                   password=request.POST['password1'])
                user.save() #lo guarda en bd
                login(request, user) #crea el cookie de sesion
                return redirect('tasks') #HttpResponse("user created")   
            except IntegrityError: 
                return render(request, 'regis.html', {
                    'form' : UserCreationForm,
                    "error": "no creado"
                })                           
    
        return render(request, 'regis.html', {
        'form' : UserCreationForm,
        'error': "Siris mal passw"
        })
       # HttpResponse("OSiris mal passw")

def tarea(request):
    return render(request, 'tasks.html')

def salir(request):
    logout(request) #quita cookie sesion
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form' : AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'],
                            password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
        'form' : AuthenticationForm,
        'error': 'no sos nadie en bd'
        })
        else:
            login(request, user)
            return redirect('tasks')
    
    
    