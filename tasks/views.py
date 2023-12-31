from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')


def regis(request):
    
    if request.method == 'GET':
        return render(request, 'regis.html', {
        'form' : UserCreationForm
    })
    else:
        if request.POST['password1'] ==  request.POST['password2']:
            try:
                user = User.Objects.create_user(username=request.POST['username'], 
                                            password=request.POST['password1'])
                user.save()
                return HttpResponse("user created")   
            except:
                return HttpResponse("no creado")             
    
        return HttpResponse("OSiris mal passw")
