# -*- coding: utf-8 -*-

"""
Autores:
    - Juan José Sánchez Troncoso
    - José Miguel Mata Boza
    - Pablo García Moya
    - Francisco Rodríguez García
"""

class Capitulo(object):
    # ATRIBUTOS
    visto = False

    # CONSTRUCTOR
    def __init__(self):
        self.visto = False
    
    # GETTERS Y SETTERS
    def get_visto(self):
        return self.visto
    
    def set_visto(self, visto):
        self.visto = visto