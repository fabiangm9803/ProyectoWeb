from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
import requests


def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login1")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form':registro})

def home(request):
    alimento = Producto.objects.all()
    context = {'alimento' :alimento}
    if request.session.get("modificado", None):
        context["modificado"]= True
        del request.session["modificado"] 
    suscrito(request, context)
    print(context)
    return render(request, "core/demo.html", context)

   # return render(request, 'core/demo.html', {'alimento':alimento, "carro":request.session.get("carro", [])})

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")   
            context["mensaje"] =  resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, "core/suscripcion.html", context)
    else:
        suscrito(request, context)
        return render(request, "core/suscripcion.html", context)

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]


def logout(request):
    return logout_then_login(request, login_url="login1")


def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login1")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total 
    venta.save()
   # messages.seccess(request, "Compra realizada")
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        
        detalle.producto.stock -= detalle.cantidad
        detalle.producto.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login1")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {"compras":compras})


def carrito(request):
    context ={}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"]= carro
    return render(request, 'core/carrito.html', context)
    #return render(request, 'core/carrito.html', {"carro":request.session.get("carro", [])})

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")


def addtocar(request, codigo):
    producto =Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:    
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")


def login1(request):
    return render(request, 'core/login1.html')

def accesorios(request):
    accesorios = Producto.objects.filter(categoria="accesorios")
    return render(request, 'core/accesorios.html', {'accesorios':accesorios, "carro":request.session.get("carro",[])})



def alimento(request):
    alimento = Producto.objects.filter(categoria="alimento")
    return render(request, 'core/alimento.html', {'alimento':alimento, "carro":request.session.get("carro",[])})



