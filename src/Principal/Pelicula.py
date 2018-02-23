# -*- coding: utf-8 -*-

"""
Autores:
    - Juan José Sánchez Troncoso
    - José Miguel Mata Boza
    - Pablo García Moya
    - Francisco Rodríguez García
"""

class Pelicula(object):
    # ATRIBUTOS
    id = ""
    titulo = ""
    fechaEstreno = ""
    generos = ""
    director = ""
    duracion = ""

    # CONSTRUCTOR
    def __init__(self, id, titulo, fechaEstreno, generos, director, duracion):
        self.id = id
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.generos = generos
        self.director = director
        self.duracion = duracion
    
    # GETTERS
    def get_titulo(self):
        return self.titulo
    
    # MÉTODOS
    def to_string(self):
        cadena = "ID: " + self.id + " | Tít: " + self.titulo + " | Año: " + self.fechaEstreno[6:10] + " | Gén: " + self.generos + " | Dir: " + self.director + " | Dur: " + self.duracion
        return cadena