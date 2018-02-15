# -*- coding: utf-8 -*-
from __builtin__ import str
from Usuario import Usuario

mi_lista = []

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
    print("=========================")
    print("|| REGISTRO DE USUARIO ||")
    print("=========================")
    nick = raw_input(">>> Nombre: ")
    edad = input(">>> Edad: ")
    clave = raw_input(">>> Contraseña: ")
    usuario = Usuario(nick, edad, clave)
    mi_lista.append(usuario)
    
    mostrarMenuUsuario()
    
    #print("Aqui mostramos al usuario:")
    #print usuario.recoger()

def inicioSesion():
    print("====================")
    print("|| INICIAR SESIÓN ||")
    print("====================")
    nick = raw_input(">>> Nombre: ")
    clave = raw_input(">>> Contraseña: ")
    
    for usuario in mi_lista:
        hayError = True
        
        if (nick == usuario.get_nombre() and clave == usuario.get_clave()):
            hayError = False
    
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
    print("4. Salir\n")
    opcion = solicitarOpcion(">>> Opción: ", 3)

def tratarOpcionMenuDamflix(opcion):
    switcher = {
        1: mostrarMenuPeliculas,
        2: mostrarMenuSeries,
        3: mostrarMenuUsuario
    }
    
    opcionATratar = switcher.get(opcion, lambda: "¡Hasta pronto!")
    
    return opcionATratar()

mostrarMenuUsuario()



