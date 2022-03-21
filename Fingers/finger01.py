# Partido de Tenis 
def duracion_partido(horas, minutos, segundos):
    ''' Duracion del partido: 11hs, 6min, 23seg.
    
        Calcular el tiempo del partido en segundos.
        
        Calculo -> [(hs * 60) + min ] * 60 + seg
    
    '''
   
    resultado = (horas * 60 * 60) + (minutos * 60) + segundos
    return print ('El tiempo de partido en segundos es: ' + str(resultado) + ' segundos.')

duracion_partido(11, 6, 23)
