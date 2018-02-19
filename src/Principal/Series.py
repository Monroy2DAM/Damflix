# -*- coding: utf-8 -*-

class Series(object):
    # Propiedades
    id = ""
    titulo = ""
    fechaEstreno = ""
    generos = ""
    duracion = ""
    temporadas = []

    # Constructor
    def __init__(self, id, titulo, fechaEstreno, generos, duracion, temporadas):
        self.id = id
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.generos = generos
        self.duracion = duracion
        self.temporadas = temporadas
    
    def to_string(self):
        cadena = self.id + " " + self.titulo + " " + self.fechaEstreno + " " + self.generos + " " + self.duracion + " " + self.temporadas
        return cadena