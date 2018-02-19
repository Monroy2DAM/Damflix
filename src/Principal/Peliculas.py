# -*- coding: utf-8 -*-

class Peliculas(object):
    # Propiedades
    id = ""
    titulo = ""
    fechaEstreno = ""
    generos = ""
    director = ""
    duracion = ""

    # Constructor
    def __init__(self, id, titulo, fechaEstreno, generos, director, duracion):
        self.id = id
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.generos = generos
        self.director = director
        self.duracion = duracion
    
    def to_string(self):
        cadena = "ID: " + self.id + " - Título: " + self.titulo + " - Fecha: " + self.fechaEstreno + " - Géneros: " + self.generos + " - Director " + self.director + " - Duración: " + self.duracion
        return cadena