# -*- coding: utf-8 -*-
import getpass
import sys
from __builtin__ import str, int
from Usuario import Usuario
from Peliculas import Peliculas
from Series import Series

global_usuario = Usuario
lista_usuarios = []
lista_peliculas = []
lista_series = []

# Se leen los ficheros de películas y series, y se cargan en sus respectivas listas.
def leerFicheros():
    archivoPeliculas = open("../bd/peliculas.txt", "r")
    
    for linea in archivoPeliculas.readlines():
        listaDatosPelicula = linea.split(";")
        pelicula = Peliculas(listaDatosPelicula[0], listaDatosPelicula[1], listaDatosPelicula[2], listaDatosPelicula[3], listaDatosPelicula[4], listaDatosPelicula[5])
        lista_peliculas.append(pelicula)
        
    archivoPeliculas.close()
    
    archivoSeries = open("../bd/series.txt", "r")

    for linea in archivoSeries.readlines():
        listaDatosSerie = linea.split(";")
        
        numeroTemporadas = listaDatosSerie[6];
        numeroCapitulos = listaDatosSerie[7];
        lista_temporadas = []
        
        for contador in range(0, int(numeroTemporadas)):
            lista_temporadas.append(numeroCapitulos)
        
        serie = Series(listaDatosSerie[0], listaDatosSerie[1], listaDatosSerie[2], listaDatosSerie[3], listaDatosSerie[4], listaDatosSerie[5], lista_temporadas)
        lista_series.append(serie)
    
    archivoSeries.close()

# Se muestra el menú de usuario.
def mostrarMenuUsuario():
    print
    print("==================")
    print("|| MENÚ USUARIO ||")
    print("==================")
    print("[1] Registrarse.")
    print("[2] Iniciar sesión.")
    print("[3] Salir.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 3)
    tratarOpcionMenuUsuario(opcion)

# Se solicita una opción.
def solicitarOpcion(mensaje, opcionMaxima):
    while True:
        opcion = input(mensaje)
        
        if (opcion >= 0 and opcion <= opcionMaxima):
            break
    
    return opcion

# Se trata una opción dada.
def tratarOpcionMenuUsuario(opcion):
    switcher = {
        1: registro,
        2: inicioSesion
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

# Se registra a un usuario.
def registro():
    global lista_usuarios
    global global_usuario
    
    print
    print("=========================")
    print("|| REGISTRO DE USUARIO ||")
    print("=========================")
    
    while True:
        nick = raw_input(">>> Nombre: ")
        
        if (len(nick) > 0):
            break
        else:
            print("[ERROR] Introduce al menos un carácter.")
            
    while 1:
        edad = raw_input(">>> Edad: ")
        
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("[ERROR] Introduce un número válido.")
    
    while True:
        clave = raw_input(prompt = ">>> Contraseña: ")
        
        if (len(clave) > 0):
            break
        else:
            print("[ERROR] Introduce al menos un carácter.")
    
    usuario = Usuario(nick, edad, clave)
    #global_usuario = None
    global_usuario = usuario
    lista_usuarios.append(global_usuario)
    mostrarMenuUsuario()

def inicioSesion():
    global lista_usuarios
    
    print
    print("====================")
    print("|| INICIAR SESIÓN ||")
    print("====================")
    nick = raw_input(">>> Nombre: ")
    clave = raw_input(">>> Contraseña: ")
    
    for usuario in lista_usuarios:
        hayError = True
        
        if (nick == usuario.get_nombre() and clave == usuario.get_clave()):
            hayError = False
            global global_usuario
            global_usuario = usuario
            break
    
    if (hayError):
        print("\n[ERROR] Credenciales incorrectas.\n")
        mostrarMenuUsuario()

    else:
        mostrarMenuDamflix()

def mostrarMenuDamflix():
    global global_usuario
    
    print
    print("=============")
    print("|| DAMFLIX ||")
    print("=============")
    print("[1] Menú películas.")
    print("[2] Menú series.")
    print("[3] Cerrar sesión.")
    print("[4] Salir.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 4)
    
    tratarOpcionMenuDamflix(opcion)

def tratarOpcionMenuDamflix(opcion):
    switcher = {
        1: mostrarMenuPeliculas,
        2: mostrarMenuSeries,
        3: mostrarMenuUsuario
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

def mostrarMenuPeliculas():
    print
    print("=========================")
    print("|| DAMFLIX - PELÍCULAS ||")
    print("=========================")
    print("[1] Ver catálogo.")
    print("[2] Marcar película como vista.")
    print("[3] Ver lista de películas vista.")
    print("[4] Marcar película para ver.")
    print("[5] Ver lista de películas para ver.")
    print("[6] Volver atrás.\n")
    opcion = solicitarOpcion(">>> Opción: ", 6)
    tratarOpcionMenuPeliculas(opcion)
    
def tratarOpcionMenuPeliculas(opcion):
    switcher = {
        1: verCatalogoPeliculas,
        2: marcarPeliculaVista,
        3: verListaPeliculasVistas,
        4: marcarPeliculaParaVer,
        5: verListaPeliculasPorVer,
        6: mostrarMenuDamflix
    }
    
    opcionATratar = switcher.get(opcion)
    
    return opcionATratar()
    
def verCatalogoPeliculas():
    for pelicula in lista_peliculas:
        print pelicula.to_string()
    
    mostrarMenuPeliculas()
    
def marcarPeliculaVista():
    global global_usuario
    
    opcion = solicitarOpcion(">>> ID de la película: ", len(lista_peliculas))
    pelicula = lista_peliculas[opcion - 1]
    global_usuario.anhadir_pelicula_vista(pelicula)
    mostrarMenuPeliculas()
    
def verListaPeliculasVistas():
    global global_usuario
    
    for pelicula in global_usuario.get_peliculas_vistas():
        print pelicula.to_string()
    
    mostrarMenuPeliculas()
    
def marcarPeliculaParaVer():
    global global_usuario
    
    opcion = solicitarOpcion(">>> ID de la película: ", len(lista_peliculas))
    pelicula = lista_peliculas[opcion - 1]
    global_usuario.anhadir_pelicula_por_ver(pelicula)
    mostrarMenuPeliculas()
    
def verListaPeliculasPorVer():
    global global_usuario
    
    for pelicula in global_usuario.get_peliculas_por_ver():
        print pelicula.to_string()
    
    mostrarMenuPeliculas()
    
def mostrarMenuSeries():
    print
    print("======================")
    print("|| DAMFLIX - SERIES ||")
    print("======================")
    print("[1] Ver catálogo.")
    print("[2] Marcar serie como vista.")
    print("[3] Ver lista de series vistas.")
    print("[4] Marcar serie para ver.")
    print("[5] Ver lista de series para ver.")
    print("[6] Marcar capítulo visto.")
    print("[7] Ver lista de capíulos vistos.")
    print("[8] Volver atrás.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 8)
    tratarOpcionMenuSeries(opcion)
    
def tratarOpcionMenuSeries(opcion):
    switcher = {
        1: verCatalogoSeries,
        2: marcarSerieVista,
        3: verListaSeriesVistas,
        4: marcarSerieParaVer,
        5: verListaSeriesPorVer,
        #6: marcarCapituloVisto,
        #7: verListaCapitulosVistos,
        8: mostrarMenuDamflix
    }
    
    opcionATratar = switcher.get(opcion)
    
    return opcionATratar()

def verCatalogoSeries():
    for serie in lista_series:
        print serie.to_string()
    
    mostrarMenuSeries()
    
def marcarSerieVista():
    global global_usuario
    
    opcion = solicitarOpcion(">>> ID de la serie: ", len(lista_series))
    serie = lista_series[opcion - 1]
    global_usuario.anhadir_serie_vista(serie)
    mostrarMenuSeries()

def verListaSeriesVistas():
    global global_usuario
    
    for serie in global_usuario.get_series_vistas():
        print serie.to_string()
    
    mostrarMenuSeries()

def marcarSerieParaVer():
    global global_usuario
    
    opcion = solicitarOpcion(">>> ID de la serie: ", len(lista_series))
    serie = lista_series[opcion - 1]
    global_usuario.anhadir_serie_por_ver(serie)
    mostrarMenuSeries()

def verListaSeriesPorVer():
    global global_usuario
    
    for serie in global_usuario.get_series_por_ver():
        print serie.to_string()
    
    mostrarMenuSeries()

def marcarCapituloVisto():
    global global_usuario
    
    

leerFicheros()
mostrarMenuUsuario()
