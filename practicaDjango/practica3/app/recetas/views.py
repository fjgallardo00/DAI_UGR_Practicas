# recetas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import Receta
from .forms import RecetaForm

# Create your views here.

def set_modo(request):
    if not request.session.get('modo'):
        request.session['modo'] = 'light'
        
    if not request.session.get('change_mode'):
        request.session['change_mode'] = 'Dark'

def index(request):
    
    set_modo(request)

    grupos = request.user.groups.all()

    if(request.POST.get('button_dark_mode')):
        if(request.session['modo'] == 'light'):
            request.session['modo'] = 'dark'
            request.session['change_mode'] = 'Light'
        else:
            request.session['modo'] = 'light'
            request.session['change_mode'] = 'Dark'

    return render(request, 'index.html', {"grupos": grupos, "modo": request.session['modo'], "change_mode": request.session['change_mode']})
    
def buscar(request):
    
    set_modo(request)

    query = request.GET.get('buscar')

    qset = (
            Q(nombre__icontains=query) | 
            Q(preparación__icontains=query)
        )

    recetas = Receta.objects.filter(qset)

    return render(request, "buscar.html", {"recetas": recetas, "modo": request.session['modo'], "change_mode": request.session['change_mode']})
    
def mostrar_receta(request, id):
    
    set_modo(request)

    qset = (
        Q(id__icontains=id)
    ) 

    receta = Receta.objects.filter(qset)

    return render(request, "receta.html", {"recetas": receta, "modo": request.session['modo'], "change_mode": request.session['change_mode']})

@login_required
def formulario(request, id):

    set_modo(request)

    if request.user.is_authenticated:

        if request.method == "POST":

            if(request.POST.get('add_receta')):
                form = RecetaForm()
                return render(request, 'add_receta.html', {"form": form, "modo": request.session['modo'], "change_mode": request.session['change_mode']})
            else:
                receta = Receta.objects.get(id=id)
                form = RecetaForm(instance=receta)
                return render(request, 'editar_receta.html', {"receta":receta, "form": form,"modo": request.session['modo'], "change_mode": request.session['change_mode']})
    else:
        return render(request, 'registration/login.html', {"modo": request.session['modo'], "change_mode": request.session['change_mode']})

@login_required
def add_receta(request):
    
    set_modo(request)

    if request.method == "POST":

        form = RecetaForm(request.POST, request.FILES)

        if form.is_valid():
            receta = form.save()
            messages.success(request, "La receta se ha creado correctamente.")
            return redirect('/mostrar_receta/'+str(receta.id))
        else:
            return render(request, 'add_receta.html', {"form": form, "modo": request.session['modo'], "change_mode": request.session['change_mode']})

    else:
        form = RecetaForm()
    
    return render(request, 'editar_receta.html', {"form": form, "modo": request.session['modo'], "change_mode": request.session['change_mode']})

@login_required
def editar_receta(request, id):
    
    set_modo(request)

    receta = Receta.objects.get(id=id)

    if request.method == "POST":

        form = RecetaForm(request.POST, request.FILES, instance=receta)

        if form.is_valid():
            receta = form.save()
            messages.success(request, "La receta se ha modificado correctamente.")
            return redirect('/mostrar_receta/'+str(receta.id))
        else:
            return render(request, 'editar_receta.html', {"receta":receta, "form": form, "modo": request.session['modo'], "change_mode": request.session['change_mode']})

    else:
        form = RecetaForm(instance=receta)
    
    return render(request, 'editar_receta.html', {"receta":receta, "form": form, "modo": request.session['modo'], "change_mode": request.session['change_mode']})

@login_required
def eliminar_receta(request, id):

    set_modo(request)

    qset = (
        Q(id__icontains=id)
    )

    Receta.objects.filter(qset).delete()

    messages.success(request, "La receta se ha eliminado correctamente.")
    return redirect(request.META['HTTP_REFERER'])

    #return render(request, 'index.html', {"modo": request.session['modo'], "change_mode": request.session['change_mode']})

def modo(request):
    
    if(request.session['modo'] == 'light'):
        request.session['modo'] = 'dark'
        request.session['change_mode'] = 'Light'
    else:
        request.session['modo'] = 'light'
        request.session['change_mode'] = 'Dark'

    return redirect(request.META['HTTP_REFERER'])
    #return render(request, 'index.html', {"modo": request.session['modo'], "change_mode": request.session['change_mode']})
