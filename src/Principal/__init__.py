# -*- coding: utf-8 -*-

"""
Autores:
    - Juan José Sánchez Troncoso
    - José Miguel Mata Boza
    - Pablo García Moya
    - Francisco Rodríguez García
"""

from __builtin__ import str, int
from Usuario import Usuario
from Pelicula import Pelicula
from Serie import Serie

"""
//=======================================================================================
// VARIABLES GLOBALES
//=======================================================================================
"""
global_usuario = Usuario
lista_usuarios = []
lista_peliculas = []
lista_series = []

"""
//=======================================================================================
// LECTURA DE FICHEROS
//=======================================================================================
"""
# Lee los ficheros de películas y series, y los carga en sus respectivas listas.
def leerFicheros():
    archivoPeliculas = open("../bd/peliculas.txt", "r")
    
    for linea in archivoPeliculas.readlines():
        listaDatosPelicula = linea.split(";")
        pelicula = Pelicula(listaDatosPelicula[0], listaDatosPelicula[1], listaDatosPelicula[2], listaDatosPelicula[3], listaDatosPelicula[4], listaDatosPelicula[5])
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
        
        serie = Serie(listaDatosSerie[0], listaDatosSerie[1], listaDatosSerie[2], listaDatosSerie[3], listaDatosSerie[4], listaDatosSerie[5], lista_temporadas)
        lista_series.append(serie)
    
    archivoSeries.close()

"""
//=======================================================================================
// MÉTODOS DEL MENÚ USUARIO
//=======================================================================================
"""
# Muestra el menú de usuario.
def mostrarMenuUsuario():
    print
    print("======================")
    print("|| ~ MENÚ USUARIO ~ ||")
    print("======================")
    print("[1] Registrarse.")
    print("[2] Iniciar sesión.")
    print("[3] Salir.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 3)
    tratarOpcionMenuUsuario(opcion)

# Solicita una opción, desde 0 hasta un límite marcado.
def solicitarOpcion(mensaje, opcionMaxima):
    while True:
        opcion = input(mensaje)
        
        if (opcion >= 0 and opcion <= opcionMaxima):
            break
    
    return opcion

# Trata una opción dada en el menú usuario.
def tratarOpcionMenuUsuario(opcion):
    switcher = {
        1: registro,
        2: inicioSesion
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

# Registra a un usuario.
def registro():
    global lista_usuarios
    global global_usuario
    global lista_series
    
    print
    print("=============================")
    print("|| ~ REGISTRO DE USUARIO ~ ||")
    print("=============================")
    
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
    
    usuario = Usuario(nick, edad, clave, lista_series)
    global_usuario = usuario
    lista_usuarios.append(global_usuario)
    
    mostrarMenuUsuario()

# Inicia la sesión de un usuario.
def inicioSesion():
    global lista_usuarios
    global global_usuario
    
    print
    print("========================")
    print("|| ~ INICIAR SESIÓN ~ ||")
    print("========================")
    
    while True:
        nick = raw_input(">>> Nombre: ")
        
        if (len(nick) > 0):
            break
        else:
            print("[ERROR] Introduce al menos un carácter.")
    
    while True:
        clave = raw_input(prompt = ">>> Contraseña: ")
        
        if (len(clave) > 0):
            break
        else:
            print("[ERROR] Introduce al menos un carácter.")
    
    for usuario in lista_usuarios:
        hayError = True
        
        if (nick == usuario.get_nombre() and clave == usuario.get_clave()):
            hayError = False
            global_usuario = usuario
            break
    
    if (hayError):
        print("\n[ERROR] Credenciales incorrectas.")
        mostrarMenuUsuario()

    else:
        mostrarMenuDamflix()

"""
//=======================================================================================
// MÉTODOS DEL MENÚ DAMFLIX
//=======================================================================================
"""
# Muestra el menú Damflix.
def mostrarMenuDamflix():
    global global_usuario
    
    print
    print("=================")
    print("|| ~ DAMFLIX ~ ||")
    print("=================")
    print("[1] Menú películas.")
    print("[2] Menú series.")
    print("[3] Cerrar sesión.")
    print("[4] Salir.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 4)
    tratarOpcionMenuDamflix(opcion)

# Trata una opción dada en el menú Damflix.
def tratarOpcionMenuDamflix(opcion):
    switcher = {
        1: mostrarMenuPeliculas,
        2: mostrarMenuSeries,
        3: mostrarMenuUsuario
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

"""
//=======================================================================================
// MÉTODOS DEL MENÚ PELÍCULAS
//=======================================================================================
"""
# Muestra el menú películas.
def mostrarMenuPeliculas():
    print
    print("=============================")
    print("|| ~ DAMFLIX - PELÍCULAS ~ ||")
    print("=============================")
    print("[1] Ver catálogo.")
    print("[2] Marcar película como vista.")
    print("[3] Ver lista de películas vista.")
    print("[4] Marcar película para ver.")
    print("[5] Ver lista de películas para ver.")
    print("[6] Volver atrás.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 6)
    tratarOpcionMenuPeliculas(opcion)

# Trata una opción dada en el menú películas.
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

# Muestra el catálogo de películas.
def verCatalogoPeliculas():
    
    print
    print("============================")
    print("|| ~ CATÁLOGO PELÍCULAS ~ ||")
    print("============================")
    
    if (len(lista_peliculas) == 0):
        print("No hay películas en el catálogo.")
    else:
        for pelicula in lista_peliculas:
            print(pelicula.to_string())
        
    mostrarMenuPeliculas()

# Marca una película como vista.
def marcarPeliculaVista():
    global global_usuario
    
    print
    print("===============================")
    print("|| ~ MARCAR PELÍCULA VISTA ~ ||")
    print("===============================")
    
    id_pelicula = solicitarOpcion(">>> ID de la película: ", len(lista_peliculas))
    pelicula = lista_peliculas[id_pelicula - 1]
    global_usuario.anhadir_pelicula_vista(pelicula)
    
    print("[INFO] Marcada como vista: " + pelicula.get_titulo())
    
    mostrarMenuPeliculas()
    
# Muestra las películas vistas.
def verListaPeliculasVistas():
    global global_usuario
    
    print
    print("================================")
    print("|| ~ LISTA PELÍCULAS VISTAS ~ ||")
    print("================================")
    
    for pelicula in global_usuario.get_peliculas_vistas():
        print(pelicula.to_string())
    
    mostrarMenuPeliculas()

# Marca una película para ver.
def marcarPeliculaParaVer():
    global global_usuario
    
    print
    print("==================================")
    print("|| ~ MARCAR PELÍCULA PARA VER ~ ||")
    print("==================================")
    
    id_pelicula = solicitarOpcion(">>> ID de la película: ", len(lista_peliculas))
    pelicula = lista_peliculas[id_pelicula - 1]
    global_usuario.anhadir_pelicula_por_ver(pelicula)
    
    print("[INFO] Marcada para ver: " + pelicula.get_titulo())
    
    mostrarMenuPeliculas()

# Muestra la lista de películas por ver.
def verListaPeliculasPorVer():
    global global_usuario
    
    print
    print("==================================")
    print("|| ~ LISTA PELÍCULAS PARA VER ~ ||")
    print("==================================")
    
    for pelicula in global_usuario.get_peliculas_por_ver():
        print(pelicula.to_string())
    
    mostrarMenuPeliculas()

"""
//=======================================================================================
// MÉTODOS DEL MENÚ SERIES
//=======================================================================================
"""
# Muestra el menú de series.
def mostrarMenuSeries():
    print
    print("==========================")
    print("|| ~ DAMFLIX - SERIES ~ ||")
    print("==========================")
    print("[1] Ver catálogo.")
    print("[2] Marcar serie como vista.")
    print("[3] Ver lista de series vistas.")
    print("[4] Marcar serie para ver.")
    print("[5] Ver lista de series para ver.")
    print("[6] Marcar capítulo visto.")
    print("[7] Ver lista de capítulos vistos.")
    print("[8] Volver atrás.\n")
    
    opcion = solicitarOpcion(">>> Opción: ", 8)
    tratarOpcionMenuSeries(opcion)

# Trata una opción dada en el menú de series.
def tratarOpcionMenuSeries(opcion):
    switcher = {
        1: verCatalogoSeries,
        2: marcarSerieVista,
        3: verListaSeriesVistas,
        4: marcarSerieParaVer,
        5: verListaSeriesPorVer,
        6: marcarCapituloVisto,
        7: verListaCapitulosVistos,
        8: mostrarMenuDamflix
    }
    
    opcionATratar = switcher.get(opcion)
    
    return opcionATratar()

# Muestra el catálogo de series.
def verCatalogoSeries():
    global global_usuario
    
    print
    print("=========================")
    print("|| ~ CATÁLOGO SERIES ~ ||")
    print("=========================")
    
    for serie in global_usuario.get_series():
        print(serie.to_string())
    
    mostrarMenuSeries()
    
# Marca una serie como vista.
def marcarSerieVista():
    global global_usuario
    
    print
    print("============================")
    print("|| ~ MARCAR SERIE VISTA ~ ||")
    print("============================")
    
    id_serie = solicitarOpcion(">>> ID de la serie: ", len(global_usuario.get_series()))
    serie = global_usuario.get_series()[id_serie - 1]
    global_usuario.anhadir_serie_vista(serie)
    serie.marcar_todos_capitulos_vistos()
    
    print("[INFO] Marcada como vista: " + serie.get_titulo())
    
    mostrarMenuSeries()

# Muestra las de series vistas.
def verListaSeriesVistas():
    global global_usuario
    
    print
    print("=============================")
    print("|| ~ LISTA SERIES VISTAS ~ ||")
    print("=============================")
    
    for serie in global_usuario.get_series_vistas():
        print(serie.to_string())
    
    mostrarMenuSeries()

# Marca una serie para ver.
def marcarSerieParaVer():
    global global_usuario
    
    print
    print("===============================")
    print("|| ~ MARCAR SERIE PARA VER ~ ||")
    print("===============================")
    
    id_serie = solicitarOpcion(">>> ID de la serie: ", len(global_usuario.get_series()))
    serie = global_usuario.get_series()[id_serie - 1]
    global_usuario.anhadir_serie_por_ver(serie)
    
    print("[INFO] Marcada para ver: " + serie.get_titulo())
    
    mostrarMenuSeries()

# Muestra las series por ver.
def verListaSeriesPorVer():
    global global_usuario
    
    print
    print("===============================")
    print("|| ~ LISTA SERIES PARA VER ~ ||")
    print("===============================")
    
    for serie in global_usuario.get_series_por_ver():
        print(serie.to_string())
    
    mostrarMenuSeries()

# Marca un capítulo como visto.
def marcarCapituloVisto():
    global global_usuario
    
    print
    print("===============================")
    print("|| ~ MARCAR CAPÍTULO VISTO ~ ||")
    print("===============================")
    
    id_serie = solicitarOpcion(">>> ID de la serie: ", len(global_usuario.get_series()))
    serie = global_usuario.get_series()[id_serie - 1]
    
    print("[INFO] Serie seleccionada: " + serie.get_titulo() + " | Temporadas: " + str(serie.get_numero_temporadas()) + " | Capítulos por temporada: " + str(serie.get_numero_capitulos()))
    
    numero_temporada = solicitarOpcion(">>> Número de la temporada: ", serie.get_numero_temporadas())
    numero_capitulo = solicitarOpcion(">>> Número del capítulo: ", serie.get_numero_capitulos())
    serie.marcar_capitulo_visto(numero_temporada, numero_capitulo)
    print("[INFO] Marcado capítulo como visto: " + str(numero_temporada) + "x" + str(numero_capitulo))
    
    if (serie.comprobar_serie_vista() == True):
        global_usuario.anhadir_serie_vista(serie)
        print("¡Enhorabuena! Ya has completado la serie :)")
    
    mostrarMenuSeries()
    
# Muestra los capítulos vistos.
def verListaCapitulosVistos():
    global global_usuario
    
    print
    print("===================================")
    print("|| ~ LISTA DE CAPÍTULOS VISTOS ~ ||")
    print("===================================")
    
    id_serie = solicitarOpcion(">>> ID de la serie: ", len(global_usuario.get_series()))
    serie = global_usuario.get_series()[id_serie - 1]
    
    print("[INFO] Serie seleccionada: " + serie.get_titulo() + " | Temporadas: " + str(serie.get_numero_temporadas()) + " | Capítulos por temporada: " + str(serie.get_numero_capitulos()))
    
    print(serie.mostrarCapitulosVistos())
    
    mostrarMenuSeries()

"""
//=======================================================================================
// PRINCIPAL
//=======================================================================================
"""
leerFicheros()
mostrarMenuUsuario()