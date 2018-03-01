# -*- coding: utf-8 -*-

"""
Autores:
    - Francisco Rodríguez García
    - Juan José Sánchez Troncoso
    - José Miguel Mata Boza
    - Pablo García Moya
    - Francisco de Asis Marquez Montoya
"""

from Capitulo import Capitulo

class Serie(object):
    # ATRIBUTOS
    id = ""
    titulo = ""
    fechaEstreno = ""
    generos = ""
    director = ""
    duracion = ""
    temporadas = [] # Lista cuyo tamaño es el número de temporadas, y el contenido de cada índice es el número de capítulos de esa temporada.
    capitulosVistos = [] # Lista que contiene una lista anidada por cada temporada. Cada lista anidada tiene los capítulos de esa temporada.

    # CONSTRUCTOR
    def __init__(self, id, titulo, fechaEstreno, generos, director, duracion, temporadas):
        self.id = id
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.generos = generos
        self.director = director
        self.duracion = duracion
        self.temporadas = temporadas
        self.capitulosVistos = []
        
        # Se recorren las temporadas.
        for temporada in self.temporadas:
            # Por cada temporada, se crea una lista anidada en capitulosVistos.
            temporada = []
            self.capitulosVistos.append(temporada)
            
            # Por cada capítulo de la temporada, se añade una instancia de capítulo en la lista de esa temporada.
            for contador in range(0, int(self.temporadas[0])):
                capitulo = Capitulo()
                temporada.append(capitulo)
    
    # GETTERS
    def get_id(self):
        return self.id
    
    def get_titulo(self):
        return self.titulo
    
    def get_numero_temporadas(self):
        return len(self.temporadas)
    
    def get_numero_capitulos(self):
        return int(self.temporadas[0])

    # MÉTODOS
    def mostrarCapitulosVistos(self):
        cadena = ""
        contadorTemporada = 1
        
        for temporada in self.capitulosVistos:
            contadorCapitulo = 1
            
            for capitulo in temporada:
                cadena += "\n\t" + str(contadorTemporada) + "x" + str(contadorCapitulo) + ": "
                
                if (capitulo.get_visto() == False):
                    cadena += "No visto"
                    
                else:
                    cadena += "Visto"
                
                contadorCapitulo += 1
            
            contadorTemporada += 1
        
        return cadena
    
    def marcar_capitulo_visto(self, numeroTemporada, numeroCapitulo):
        capitulo = self.capitulosVistos[numeroTemporada - 1][numeroCapitulo - 1]
        capitulo.set_visto(True)
    
    def comprobar_serie_vista(self):
        todos_vistos = True
        
        for temporada in self.capitulosVistos:
            
            for capitulo in temporada:
                
                if (capitulo.get_visto() == False):
                    todos_vistos = False
                    break;
        
        return todos_vistos
    
    def marcar_todos_capitulos_vistos(self):
        for temporada in self.capitulosVistos:
            
            for capitulo in temporada:
                capitulo.set_visto(True)
    
    def to_string(self):
        cadenaTemporadas = ""
        
        for temporada in self.temporadas:
            cadenaTemporadas += temporada + ", "
        
        cadenaTemporadas = cadenaTemporadas[:-2]
        
        cadena = "ID: " + self.id + " | Tít: " + self.titulo + " | Año: " + self.fechaEstreno[6:10] + " | Gén: " + self.generos + " | Dir: " + self.director + " | Dur: " + self.duracion + " | Temps: " + str(len(self.temporadas)) + " | Caps/Temp: " + str(self.temporadas[0])
        return cadena
