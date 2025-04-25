from datetime import date
from abc import ABC, abstractmethod


class Partido(ABC):
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

    # - Se necesita pasar dos listas, con el número de juegos ganados por
    #   cada jugador en cada set. (sets1, sets2)
class Tenis(Partido):
    def __init__(self, contrincante1, contrincante2, fecha, competicion, sets1, sets2):
        super().__init__(contrincante1, contrincante2, fecha, competicion)

        # Excepción para que cada jugador tenga la misma cantidad de sets.
        
        if len(sets1) != len(sets2):
            raise ValueError("Cada jugador debe tener la misma cantidad de sets.")
        
        # - El número de sets debe ser 3 o 5, si no salta la excepción.

        total_sets = len(sets1)
        if total_sets != 3 and total_sets != 5:
            raise ValueError("Solo se permiten partidos de 3 o 5 sets.")
        
        self.sets1 = sets1
        self.sets2 = sets2

    def ganador(self):

        # Creo dos contadores, para contar cuantos sets ganó cada jugador
        # empezando desde 0

        ganados1 = 0
        ganados2 = 0
        
        #s1 y s2, variables de iteración que recogen cuantos juegos ha ganado cada
        #jugador en el mismo set.

        for s1, s2 in zip(self.sets1, self.sets2):
            # Con esto sabemos quien ganó cada set
            if s1 > s2:
                ganados1 += 1
            else:
                ganados2 += 1
            
            # Si ganados1 > ganados 2 --> ganador -> contrincante1
            # Si ganados1 < ganados 2 --> ganador -> contrincante2
        return self.contrincante1 if ganados1 > ganados2 else self.contrincante2

    def resultado(self):

        # Lista vacía donde guardará los resultados de cada set
        sets = []


        for s1, s2 in zip(self.sets1, self.sets2):
            #En este caso después de crear un string del tipo "6-4", "3-6", lo 
            #añade a la lista 
            sets.append(f"{s1}-{s2}")
            #Con el join une los sets en una sola cadena separad por comas.
        return ", ".join(sets)
        



    


    

    

    
    

