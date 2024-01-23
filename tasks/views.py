from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tarea
from django.utils import timezone
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
        'error': "Contraseñas no coinciden"
        })
       # HttpResponse("OSiris mal passw")

def tarea(request):
    tareas = Tarea.objects.filter(user= request.user, fechacompletado__isnull=True) #fechacompletado__isnull=True q la liste si no compl
    return render(request, 'tasks.html', {'tareas': tareas})

def tacompl(request):
    tareas = Tarea.objects.filter(user= request.user, fechacompletado__isnull=False).order_by('fechacompletado') #-??? se pone?
    return render(request, 'tacompl.html', {'tareas': tareas})

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
    
def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html',{
        'form' : TareaForm
        })
    else:
        try:
            form = TareaForm(request.POST) #le ponde los datos del form qse envia
            new_task = form.save(commit=False) #evita que se guarde
            new_task.user = request.user #usuario loggeado
            new_task.save()
            return redirect('tasks')
        except:
            return render (request, 'tasks.html', {
                    'error' : "tarea no sirve"
                })
            
            
def detalle_tarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user)
        form = TareaForm
        return render(request, 'detarea.html', {'tarea': tarea, 'form': form})
    else: 
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user) 
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('tasks')
        except: ValueError
        return render(request, 'detarea.html', {'tarea': tarea, 'form': form, 
                                                'error': "No es posible actualizar"})
        
        
def borrar(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user) 
    if request.method == 'POST':
        tarea.delete()
        return redirect('tasks')
    
def completa(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, user=request.user) 
    if request.method == 'POST':
        tarea.fechacompletado = timezone.now()
        tarea.save()
        return redirect('tasks')
        
        
        
            
        
    