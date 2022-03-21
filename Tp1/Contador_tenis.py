
def nombres ():
      
    '''
    Pide los nombres de los jugadores
    ''' 
    jugador_1 = input('Nombre del jugador 1?: ')
    jugador_2 = input('Nombre del jugador 2?: ') 

    return jugador_1, jugador_2

def manual ():
    
    jugador_1, jugador_2  = nombres()
    
    contador_j1 = 0
    contador_j2 = 0
    while contador_j1 < 6 or contador_j2 < 6:
        '''
        - Pregunta quien gano el punto.
        - Lleva el contador. 
        '''
        ganador_punto = input ("Quien gano el punto?: ")
    
        if ganador_punto == jugador_1 :
            contador_j1 = contador_j2 + 1 
            
        elif ganador_punto == jugador_2:
            contador_j2 = contador_j2 + 1
        
        else: 
            print('El nombre no es valido. Vuelva a ingresarlo.')
            
        '''
        - LLeva los puntajes. 
        '''            
        puntos = [0,15,30,40,'Ad']
        for puntos in range ():
            
             
        
    
    
    
    
    

def contador_tenis ():
    modo_juego = input("""Modo 1: Manual 
        Modo 2: Simulador""")
    if modo_juego == "Modo 1":
        

    
    

