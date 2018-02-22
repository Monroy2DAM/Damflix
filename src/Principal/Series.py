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
        
        cadenaTemporadas = ""
        
        for temporada in self.temporadas:
            cadenaTemporadas += temporada + ", "
        
        cadenaTemporadas = cadenaTemporadas[:-2]
        
        cadena = "ID: " + self.id + " | Título: " + self.titulo + " | Fecha: " + self.fechaEstreno + " | Géneros: " + self.generos + " | Director: " + self.director + " | Duración: " + self.duracion + " | Temporadas/Capítulos: " + cadenaTemporadas
        return cadena