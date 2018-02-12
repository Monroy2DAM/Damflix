# -*- coding: utf-8 -*-
from __builtin__ import str
from Usuario import Usuario

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
    
    print("Aqui mostramos al usuario:")
    print usuario.recoger()

def inicioSesion():
    return "Iniciar sesión"
    

mostrarMenuUsuario()

