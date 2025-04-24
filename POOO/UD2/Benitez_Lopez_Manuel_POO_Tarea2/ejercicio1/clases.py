from datetime import date


class Partido:
    def __init__(self, contrincante1, contrincante2, fecha, competicion):
        self.contrincante1 = contrincante1
        self.contrincante2 = contrincante2
        self.fecha = fecha
        self.competicion = competicion

    # a. Retornar el ganador del partido.

    def ganador(self):

        

    # b. Retornar el resultado.

    def resultado(self):
        
    

    # c. Retornar una representación del partido con el formato “xxx Vs. YYY -fecha - competición”.
    def __str__(self):
        return f"{self.contrincante1} Vs. {self.contrincante2} - {self.fecha} - {self.competicion}"
    

    # Se debe tener en cuenta que los partidos pueden ser:

    ##### Partido de fútbol:

class Futbol(Partido):
    def __init__(self, contrincante1, contrincante2, fecha, competicion, goles_contrin1, goles_contrin2)
        super().__init__(contrincante1, contrincante2, fecha, competicion)
        
        # - Lanzar una excepción raise ValueError

        if type(goles_contrin1 or goles_contrin2) < 0:
            raise ValueError("El resultado de goles no pude ser negativo")
        self.goles_contrin1 = goles_contrin1
        self.goles_contrin2 = goles_contrin2

    
    # - Puede darse el empate como resultado.
    def resultado(self, partido):
        if partido.goles_contrin1 == partido.goles_contrin2:
            return f"El partido ha quedado en empate"
    
    
    # - El resultado debe tener el formato: Zafra 4 - 5 Badajoz.
    def __str__(self):
        return f"{self.contrincante1} {self.goles_contrin1} - {self.goles_contrin2} {self.contrincante2}"
    

    ##### Partido de Baloncesto:

    # - Deben almacenarse los puntos de cada equipo.
class Baloncesto(Partido):
    def __init__(self, contrincante1, contrincante2, fecha, competicion, puntos_contrin1, puntos_contrin2):
        super().__init__(contrincante1, contrincante2, fecha, competicion)
        
        # - No puede darse el empate. Excepción
        if type(puntos_contrin1) == type(puntos_contrin2):
            raise ValueError("No puede darse el empate")
        self.puntos_contrin1 = puntos_contrin1
        self.puntos_contrin2 = puntos_contrin2

    # - El resultado debe tener el formato: 90 Cáceres - Badajoz 88.             
    def __str__(self):
        return f"{self.puntos_contrin1} {self.contrincante1} - {self.contrincante2} {self.puntos_contrin2} "
    


    ##### Partido de Tenis:
class Tenis(Partido):

    

    
    

