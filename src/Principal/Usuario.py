# -*- coding: utf-8 -*-

"""
Autores:
    - Francisco Rodríguez García
    - Juan José Sánchez Troncoso
    - José Miguel Mata Boza
    - Pablo García Moya
    - Francisco de Asis Marquez Montoya
"""

from __builtin__ import str
from Pelicula import Pelicula

class Usuario():
    # ATRIBUTOS
    nombre = ""
    clave = ""
    edad = 0
    peliculasVistas = []
    peliculasPorVer = []
    series = []
    seriesVistas = []
    seriesPorVer = []

    # CONSTRUCTOR
    def __init__(self, nombre, edad, clave, series):
        self.nombre = nombre
        self.edad = edad
        self.clave = clave
        self.peliculasVistas = []
        self.peliculasPorVer = []
        self.series = series
        self.seriesVistas = []
        self.seriesPorVer = []
    
    # GETTERS
    def get_nombre(self):
        return self.nombre
    
    def get_clave(self):
        return self.clave
    
    def get_peliculas_vistas(self):
        return self.peliculasVistas
    
    def get_peliculas_por_ver(self):
        return self.peliculasPorVer
    
    def get_series(self):
        return self.series
    
    def get_series_vistas(self):
        return self.seriesVistas
    
    def get_series_por_ver(self):
        return self.seriesPorVer
    
    # MÉTODOS
    def anhadir_pelicula_vista(self, pelicula):
        self.peliculasVistas.append(pelicula)
        
    def anhadir_pelicula_por_ver(self, pelicula):
        self.peliculasPorVer.append(pelicula)
    
    def anhadir_serie_vista(self, serie):
        self.seriesVistas.append(serie)
        
    def anhadir_serie_por_ver(self, serie):
        self.seriesPorVer.append(serie)
        
    def to_string(self):
        if self.peliculasPorVer:
            cadenaPeliculasVistas = ""
        
            for pelicula in self.peliculasVistas:
                cadenaPeliculasVistas += pelicula.to_string() + "\n"
            
            cadenaPeliculasVistas = cadenaPeliculasVistas[:-2]
        
        else:
            cadenaPeliculasVistas = "Sin películas vistas."
        
        cadena = "Nombre: " + self.nombre + " | Edad: " + str(self.edad) + " | Clave: "+ self.clave + " | Lista de películas vista:\t\n" + cadenaPeliculasVistas
        
        return cadena
