from django.shortcuts import render
from django.db import Error
from appPeliculas.models import Genero, Pelicula
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

@csrf_exempt
def agregarGenero(request):
    try:
        #recibir el nombre del genero en una variable local
        nombre = request.POST["txtNombre"]
        print(nombre)
        #crear objeto tipo Genero
        genero = Genero(genNombre=nombre)
        #salvar objeto en la base de datos
        genero.save()
        mensaje = "Genero agregado correctamente"
    except Error as error:
        mensaje = str(error)
    #return JsonResponse({"mensaje":mensaje})
    retorno = {"mensaje": mensaje}
    return render(request,"agregarGenero.html", retorno)

def vistaAgregarGeneros(request):
    return render(request, 'agregarGenero.html')

def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"Peliculas":list(peliculas)}
    return render(request,"listarPeliculas.html", retorno) 
    

def listarGeneros(request):
    generos = Genero.objects.all()
    retorno = {"generos":list(generos)}
    return render(request,"listarGeneros.html", retorno)