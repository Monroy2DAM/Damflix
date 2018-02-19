# -*- coding: utf-8 -*-
from __builtin__ import str
from Peliculas import Peliculas

class Usuario():
    # Propiedades
    nombre = ""
    clave = ""
    edad = 0
    peliculasVistas = []
    peliculasPorVer = []
    seriesVistas = []
    seriesPorVer = []

    # Constructor
    def __init__(self, nombre, edad, clave):
        self.nombre = nombre
        self.edad = edad
        self.clave = clave
    
    def to_string(self):
        cadena = self.nombre + " " + str(self.edad) + " "+ self.clave
        return cadena
    
    def get_nombre(self):
        return self.nombre
    
    def get_clave(self):
        return self.clave
    
    def get_peliculas_vistas(self):
        return self.peliculasVistas
    
    def get_peliculas_por_ver(self):
        return self.peliculasPorVer
    
    def anhadir_pelicula_vista(self, pelicula):
        self.peliculasVistas.append(pelicula)
        
    def anhadir_pelicula_por_ver(self, pelicula):
        self.peliculasPorVer.append(pelicula)