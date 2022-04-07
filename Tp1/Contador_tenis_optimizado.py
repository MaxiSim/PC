def nombres ():  
    '''
    Pide los nombres de los jugadores
    jugador_1 ____ Nombre del jugador 1
    jugador_2 ____ Nombre del jugador 2
    ''' 
    jugador_1 = input('Nombre del jugador 1?: ')
    jugador_2 = input('Nombre del jugador 2?: ') 

    return jugador_1, jugador_2

def puntos (contador_j1, contador_j2):
    '''
    Compara el contador de puntos iniciado en los diferentes modos, 
    con los valores de los puntos reales en el tenis. 
    '''
    if contador_j1 == 0:
        puntaje_j1 = 0
    if contador_j2 == 0:
        puntaje_j2 = 0
    
    if contador_j1 == 1:
        puntaje_j1 = 15
    if contador_j2 == 1:
        puntaje_j2 = 15
    if contador_j1 == 2:
        puntaje_j1 = 30
    if contador_j2 == 2:
        puntaje_j2 = 30
        
    if contador_j1 == 3:
        puntaje_j1 = 40
    if contador_j2 == 3:
        puntaje_j2 = 40
    
    if contador_j1 == 4:
        puntaje_j1 = 'Ad'
    if contador_j2 == 4:
        puntaje_j2 = 'Ad'
        
    if contador_j1 == 5:
        puntaje_j1 = 'Ganador'
    if contador_j2 == 5:
        puntaje_j2 = 'Ganador'
    
    return puntaje_j1, puntaje_j2
        

def manual ():
    
    jugador_1, jugador_2  = nombres()
    contador_j1 = 0
    contador_j2 = 0
    ganador = ''

    '''
    Pregunta quien gano el punto. 
    Lleva un contador para cada jugador.
    Imprime los puntos durante todo el game.
    Imprime el ganador del game.
        
    contador_j1 ----- Contador que lleva el puntaje del J1.
    contador_j2 ----- Contador que lleva el puntaje del J2.
    ganador_punto --- Guarda el input del usuario sobre que jugador metio el punto.
    puntaje_j1 ------ Transforma el numero del contador_j1 en los puntos reales del game. 
    puntaje_j2 ------ Transforma el numero del contador_j2 en los puntos reales del game.
    ganador --------- Guarda el nombre del ganador del game.
        
    Devuelve None 
    '''

    while contador_j1 != 5 and contador_j2 != 5:
        
        ganador_punto = input ("Quien gano el punto?: ")
    
        if contador_j1 < 3 and contador_j2 < 3:    
            if ganador_punto == jugador_1 :
                contador_j1 += 1     
            elif ganador_punto == jugador_2:
                contador_j2 += 1
            else: 
                print('El nombre no es valido. Vuelva a ingresarlo.')
                  
        elif contador_j1 == 3 and contador_j2 < 3 and ganador_punto == jugador_1:
            contador_j1 += 2
            
        elif contador_j1 < 3 and contador_j2 == 3 and ganador_punto == jugador_2:
            contador_j2 += 2
            
        elif contador_j1 == 3 and contador_j2 < 3 and ganador_punto == jugador_2:
            contador_j2 += 1
            
        elif contador_j1 < 3 and contador_j2 == 3 and ganador_punto == jugador_1:
            contador_j1 += 1
            
        elif contador_j1 == 3 and contador_j2 == 3:
            if ganador_punto == jugador_1:
                contador_j1 += 1
            elif ganador_punto == jugador_2:
                contador_j2 += 1
                
        elif contador_j1 == 4 and ganador_punto == jugador_2:
            contador_j1 -= 1
        elif contador_j2 == 4 and ganador_punto == jugador_1:
            contador_j2 -= 1
            
        elif contador_j1 == 4 and ganador_punto == jugador_1:
            contador_j1 += 1
        elif contador_j2 == 4 and ganador_punto == jugador_2:
            contador_j2 += 1
            
        puntaje_j1, puntaje_j2 = puntos(contador_j1, contador_j2)
        
        print('Tabla de puntos:')    
        print(jugador_1, ': ' , puntaje_j1)
        print(jugador_2, ': ' , puntaje_j2)
   
    if puntaje_j1 == 'Ganador':
        ganador = jugador_1
    elif puntaje_j2 == 'Ganador':
        ganador = jugador_2
    print('El ganador fue: ', ganador )
        
    return None
       
       
def simulador ():
    import random
    jugador_1, jugador_2  = nombres()
    tipo_info = input('''
        1. Desarrollado
        2. Directo 
        ''')
    contador_j1 = 0
    contador_j2 = 0
    ganador = ''
    
    '''
    Genera de manera random el ganador de cada punto.
    Lleva un contador para cada jugador.
    Pregunta si se quiere ver todo el juego o solo el resultado final. 
    Imprime los puntos durante todo el game o imprime el ganador del game.
        
    tipo_info ------- Guarda el modo de visualizacion del partido. 
    contador_j1 ----- Contador que lleva el puntaje del J1.
    contador_j2 ----- Contador que lleva el puntaje del J2.
    ganador_punto --- Guarda el valor del random para ver quien gano el punto.
    puntaje_j1 ------ Transforma el numero del contador_j1 en los puntos reales del game. 
    puntaje_j2 ------ Transforma el numero del contador_j2 en los puntos reales del game.
    ganador --------- Guarda el nombre del ganador del game.
        
    Devuelve None 
    '''
    while contador_j1 != 5 and contador_j2 != 5:
        
        ganador_punto = random.randint(1,2)
    
        if contador_j1 < 3 and contador_j2 < 3:    
            if ganador_punto == 1 :
                contador_j1 += 1   
            elif ganador_punto == 2:
                contador_j2 += 1
            else: 
                print('El nombre no es valido. Vuelva a ingresarlo.')
                 
        elif contador_j1 == 3 and contador_j2 < 3 and ganador_punto == 1:
            contador_j1 += 2    
        elif contador_j1 < 3 and contador_j2 == 3 and ganador_punto == 2:
            contador_j2 += 2  
        elif contador_j1 == 3 and contador_j2 < 3 and ganador_punto == 2:
            contador_j2 += 1  
        elif contador_j1 < 3 and contador_j2 == 3 and ganador_punto == 1:
            contador_j1 += 1
        elif contador_j1 == 3 and contador_j2 == 3:
            if ganador_punto == 1:
                contador_j1 += 1
            elif ganador_punto == 2:
                contador_j2 += 1   
        elif contador_j1 == 4 and ganador_punto == 2:
            contador_j1 -= 1
        elif contador_j2 == 4 and ganador_punto == 1:
            contador_j2 -= 1
        elif contador_j1 == 4 and ganador_punto == 1:
            contador_j1 += 1
        elif contador_j2 == 4 and ganador_punto == 2:
            contador_j2 += 1
        
        puntaje_j1, puntaje_j2 = puntos(contador_j1, contador_j2)
            
        if ganador_punto == 1:
            ganador_punto_II = jugador_1
        elif ganador_punto == 2:
            ganador_punto_II = jugador_2
       
        if tipo_info == "1": 
            print('¿Quien ganó el punto?', ganador_punto_II)
            print('Tabla de puntos:')    
            print(jugador_1, ': ' , puntaje_j1)
            print(jugador_2, ': ' , puntaje_j2) 
            
    if puntaje_j1 == 'Ganador':
        ganador = jugador_1
    elif puntaje_j2 == 'Ganador':
        ganador = jugador_2
    
    if tipo_info == '1':
        print('El ganador fue: ', ganador)
    elif tipo_info == '2':
        print('El ganador fue: ', ganador )
    
    return None
                

def main ():
    '''
    Funciona como un menu para el usuario. 
    Pregunta el modo de juego y lo ejecuta. 
    '''
    
    modo_juego = input("""
        Bienvenido al simulador de tenis. 
        ¿En que modo quiere jugar?                     
        1: Manual 
        2: Simulador
         """)
    if modo_juego == "1":
        manual()
    elif modo_juego == "2":
        simulador()
        
if __name__ == '__main__':
    main()