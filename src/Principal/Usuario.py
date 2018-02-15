# -*- coding: utf-8 -*-
from __builtin__ import str
'''
Created on 12 feb. 2018

@author: srk
'''

class Usuario():
    # Propiedades
    nombre=""
    clave=""
    edad=0
    peliculasVistas=[]
    peliculasPorVer=[]
    seriesVistas=[]
    seriesPorVer=[]

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