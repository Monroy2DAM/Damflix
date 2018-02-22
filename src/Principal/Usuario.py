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
        self.peliculasVistas = []
        self.peliculasPorVer = []
        self.seriesVistas = []
        self.seriesPorVer = []
    
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
    
    def get_nombre(self):
        return self.nombre
    
    def get_clave(self):
        return self.clave
    
    def get_peliculas_vistas(self):
        return self.peliculasVistas
    
    def get_peliculas_por_ver(self):
        return self.peliculasPorVer
    
    def get_series_vistas(self):
        return self.seriesVistas
    
    def get_series_por_ver(self):
        return self.seriesPorVer
    
    def anhadir_pelicula_vista(self, pelicula):
        self.peliculasVistas.append(pelicula)
        
    def anhadir_pelicula_por_ver(self, pelicula):
        self.peliculasPorVer.append(pelicula)
    
    def anhadir_serie_vista(self, serie):
        self.seriesVistas.append(serie)
        
    def anhadir_serie_por_ver(self, serie):
        self.seriesPorVer.append(serie)