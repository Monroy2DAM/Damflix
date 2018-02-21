# -*- coding: utf-8 -*-

class Series(object):
    # Propiedades
    id = ""
    titulo = ""
    fechaEstreno = ""
    generos = ""
    director = ""
    duracion = ""
    temporadas = []

    # Constructor
    def __init__(self, id, titulo, fechaEstreno, generos, director, duracion, temporadas):
        self.id = id
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.generos = generos
        self.director = director
        self.duracion = duracion
        self.temporadas = temporadas
    
    def to_string(self):
        # TODO: Pasar lista a cadena.
        cadena = self.id + " " + self.titulo + " " + self.fechaEstreno + " " + self.generos + " " + self.director + " " + self.duracion + " " + self.temporadas
        return cadena