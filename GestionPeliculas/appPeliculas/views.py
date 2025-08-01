import os
from django.conf import settings
from django.shortcuts import redirect, render
from django.db import Error
from appPeliculas.models import Genero, Pelicula
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

#CRUD Generos


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


def vistaAgregarGenero(request):
    return render(request, 'agregarGenero.html')


def listarGeneros(request):
    generos = Genero.objects.all()
    retorno = {"generos":list(generos)}
    return render(request,"listarGeneros.html", retorno)


#CRUD Peliculas


def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"Peliculas":list(peliculas)}
    return render(request,"listarPeliculas.html", retorno) 


def agregarPelicula(request):
    try:
        codigo = request.POST["txtCodigo"]
        titulo = request.POST["txtTitulo"]
        protagonista = request.POST["txtProtagonista"]
        duracion = int(request.POST["txtDuracion"])
        resumen = request.POST["txtResumen"]
        foto = request.FILES["fileFoto"]
        print(request.POST["cbGenero"])
        id_genero = request.POST["cbGenero"]
        genero = Genero.objects.get(pk=id_genero)
        #crear objeto tipo Pelicula
        pelicula = Pelicula(pelCodigo=codigo, pelTitulo=titulo, 
                            pelProtagonista=protagonista,pelDuracion=duracion,
                            pelResumen=resumen, pelFoto=foto, pelGenero=genero)
        #salvar objeto en la base de datos
        pelicula.save()
        mensaje = "Pelicula agregada correctamente"
    except Error as error:
        mensaje = str(error)
    retorno={"mensaje":mensaje, "idPelicula":pelicula.id, "generos": Genero.objects.all()}
    return render(request, "agregarPelicula.html", retorno)


def vistaAgregarPelicula(request):
    generos = Genero.objects.all()
    retorno = {"generos": generos}
    return render(request, "agregarPelicula.html", retorno)

def consultarPeliculaPorId(request, id):
    pelicula = Pelicula.objects.get(pk=id)
    generos = Genero.objects.all()
    retorno = {"pelicula": pelicula, "generos": generos}
    return render(request, "actualizarPelicula.html", retorno)

def actualizarPelicula(request):
    try:
        #recibir el id de la pelicula a actualizar
        idPelicula = request.POST["idPelicula"]
        #obtener pelicula por id
        peliculaActualizar = Pelicula.objects.get(pk=idPelicula)
        peliculaActualizar.pelCodigo = request.POST["txtCodigo"]
        peliculaActualizar.pelTitulo = request.POST["txtTitulo"]
        peliculaActualizar.pelProtagonista = request.POST["txtProtagonista"]
        peliculaActualizar.pelDuracion = int(request.POST["txtDuracion"])
        peliculaActualizar.pelResumen = request.POST["txtResumen"]
        idGenero = request.POST["cbGenero"]
        genero = Genero.objects.get(pk = idGenero)
        peliculaActualizar.pelGenero = genero
        foto = request.FILES.get("fileFoto")
        if foto:
            os.remove(os.path.join(settings.MEDIA_ROOT + "/" + str(peliculaActualizar.pelFoto)))
            peliculaActualizar.pelFoto = foto
        peliculaActualizar.save()
        mensaje = "Pelicula actualizada correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje":mensaje}
    #return JsonResponse(retorno)
    return redirect('/listarPeliculas')



def eliminarPelicula(request, id):
    try:
        peliculaEliminar = Pelicula.objects.get(pk=id)
        if peliculaEliminar is None:
            mensaje = f"Pelicula no encontrada con el id {id}.."
        else:
            foto = peliculaEliminar.pelFoto
            peliculaEliminar.delete()
            os.remove(os.path.join(settings.MEDIA_ROOT + "/" + str(foto)))
            mensaje = f"Pelicula con id={id} eliminada correctamente..."

    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    #return JsonResponse(retorno)
    return redirect('/listarPeliculas')        