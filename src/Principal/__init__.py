# -*- coding: utf-8 -*-
from __builtin__ import str
from Usuario import Usuario
from Peliculas import Peliculas
from Series import Series

global_usuario = Usuario
lista_usuarios = []
lista_peliculas = []
lista_series = []

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

def mostrarMenuUsuario():
    print("==================")
    print("|| MENÚ USUARIO ||")
    print("==================")
    print("1. Registrarse.")
    print("2. Iniciar sesión.")
    print("3. Salir.\n")
    opcion = solicitarOpcion(">>> Opción: ", 3)
    tratarOpcionMenuUsuario(opcion)

def solicitarOpcion(mensaje, opcionMaxima):
    while True:
        opcion = input(mensaje)
        
        if (opcion >= 0 and opcion <= opcionMaxima):
            break
    
    return opcion

def tratarOpcionMenuUsuario(opcion):
    switcher = {
        1: registro,
        2: inicioSesion
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

def registro():
    global lista_usuarios
    global global_usuario
    
    print("=========================")
    print("|| REGISTRO DE USUARIO ||")
    print("=========================")
    nick = raw_input(">>> Nombre: ")
    edad = input(">>> Edad: ")
    clave = raw_input(">>> Contraseña: ")
    
    usuario = Usuario(nick, edad, clave)
    global_usuario = usuario
    lista_usuarios.append(global_usuario)
    print len(lista_usuarios)
    mostrarMenuUsuario()
    
    #print("Aqui mostramos al usuario:")
    #print usuario.recoger()

def inicioSesion():
    global lista_usuarios
    
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
    print("=============")
    print("|| DAMFLIX ||")
    print("=============")
    print("1. Menú películas.")
    print("2. Menú series.")
    print("3. Cerrar Sesion.")
    print("4. Salir.\n")
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
    print("=========================")
    print("|| DAMFLIX - PELÍCULAS ||")
    print("=========================")
    print("1. Ver catálogo.")
    print("2. Marcar película como vista.")
    print("3. Ver lista de películas vista.")
    print("4. Marcar película para ver.")
    print("5. Ver lista de películas para ver.")
    print("6. Volver atrás.\n")
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
    
    print "\n"
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
    
    print "\n"
    mostrarMenuPeliculas()
    
def mostrarMenuSeries():
    print("======================")
    print("|| DAMFLIX - SERIES ||")
    print("======================")
    print("1. Ver catálogo.")
    print("2. Marcar serie como vista.")
    print("3. Ver lista de series vistas.")
    print("4. Marcar serie para ver.")
    print("5. Ver lista de series para ver.")
    print("6. Marcar capítulo visto.")
    print("7. Ver lista de capíulos vistos.")
    print("8. Volver atrás.\n")
    opcion = solicitarOpcion(">>> Opción: ", 8)
    tratarOpcionMenuSeries(opcion)
    
def tratarOpcionMenuSeries(opcion):
    switcher = {
        1: verCatalogoSeries,
        #2: marcarSerieVista,
        #3: verListaSeriessVistas,
        #4: marcarSerieParaVer,
        #5: verListaSeriesPorVer,
        #6: marcarCapituloVisto,
        #7: verListaCapitulosVistos,
        #8: mostrarMenuDamflix
    }
    
    opcionATratar = switcher.get(opcion)
    
    return opcionATratar()

def verCatalogoSeries():
    for serie in lista_series:
        print serie.to_string()
    
    mostrarMenuSeries()

leerFicheros()
mostrarMenuUsuario()
