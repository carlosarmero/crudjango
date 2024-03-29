"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('enroll/', views.regis,name='enroll'),
    path('signin/', views.signin, name='signin'),
    path('tasks/', views.tarea, name='tasks'),
    path('tacompl/', views.tacompl, name='tacompl'),
    path('tasks/<int:tarea_id>/', views.detalle_tarea, name='detarea'),
    path('tasks/crear/', views.crear_tarea, name='crear'),
    path('tasks/<int:tarea_id>/borrar', views.borrar, name='borrar'),
    path('tasks/<int:tarea_id>/completa', views.completa, name='completa'),
    path('logout/', views.salir, name='log'),
    path('tasks/logout/', views.salir), 
    path('tacompl/logout/', views.salir),
    path('tasks/<int:tarea_id>/logout/', views.salir2),
    path('tasks/crear/logout/', views.salir)     
]
