from datetime import date
from abc import ABC, abstractmethod


class Partido:
    def __init__(self, contrincante1, contrincante2, fecha, competicion):
        self.contrincante1 = contrincante1
        self.contrincante2 = contrincante2
        self.fecha = fecha
        self.competicion = competicion

    # Dado que los metodos ganador y resultado se implementan en las subclases,
    # uso metodos abstractos.
    
    # a. Retornar el ganador del partido.

    @abstractmethod
    def ganador(self):
        pass

        

    # b. Retornar el resultado.
    
    @abstractmethod
    def resultado(self):
        pass
        
    

    # c. Retornar una representación del partido con el formato “xxx Vs. YYY -fecha - competición”.
    def __str__(self):
        return f"{self.contrincante1} Vs. {self.contrincante2} - {self.fecha} - {self.competicion}"
    

    # Se debe tener en cuenta que los partidos pueden ser:

    
    
    ##### Partido de fútbol:

class Futbol(Partido):
    def __init__(self, contrincante1, contrincante2, fecha, competicion, goles_contrin1, goles_contrin2):
        super().__init__(contrincante1, contrincante2, fecha, competicion)
        
        # - Lanzar una excepción raise ValueError

        if goles_contrin1 < 0 or goles_contrin2 < 0:
            raise ValueError("El resultado de goles no pude ser negativo")
        self.goles_contrin1 = goles_contrin1
        self.goles_contrin2 = goles_contrin2

    
    
    
    
    # - Puede darse el empate como resultado.
    def ganador(self):
        if self.goles_contrin1 > self.goles_contrin2:
            return self.contrincante1
        elif self.goles_contrin1 < self.goles_contrin2:
            return self.contrincante2
        else:
            return None # Esto permite el empate



    
    
    # - El resultado debe tener el formato: Zafra 4 - 5 Badajoz.
    def resultado(self):
        return f"{self.contrincante1} {self.goles_contrin1} - {self.goles_contrin2} {self.contrincante2}"
    
    
    
    
        
    
    ##### Partido de Baloncesto:

    # - Deben almacenarse los puntos de cada equipo.
class Baloncesto(Partido):
    def __init__(self, contrincante1, contrincante2, fecha, competicion, puntos_contrin1, puntos_contrin2):
        super().__init__(contrincante1, contrincante2, fecha, competicion)
        
        # - No puede puntos negativos. Excepción.
        if puntos_contrin1 < 0 or puntos_contrin2 < 0:
            raise ValueError("Los puntos no pueden ser negativos")        
        
        # - No puede darse el empate
        if puntos_contrin1 == puntos_contrin2:
            raise ValueError("No puede haber empate")
        
        self.puntos_contrin1 = puntos_contrin1
        self.puntos_contrin2 = puntos_contrin2

    
    

    # ganador

    def ganador(self):
        if self.puntos_contrin1 > self.puntos_contrin2:
            return self.contrincante1
        elif self.puntos_contrin1 < self.puntos_contrin2:
            return self.contrincante2

             
    
    
    
    
    
    
    
    
    # - El resultado debe tener el formato: 90 Cáceres - Badajoz 88.             
    def resultado(self):
        return f"{self.puntos_contrin1} {self.contrincante1} - {self.contrincante2} {self.puntos_contrin2}"
    


    ##### Partido de Tenis:
class Tenis(Partido):


    ganados_contrin1 = []


    ganados_contrin2 = []

    

    
    

