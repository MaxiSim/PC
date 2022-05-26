

def total_gain(volume, initial_price, final_price):
    ''' 
    -- Multiplica el volumen por el costo inicial y final.
    
    -- Calcula la diferencia = ganancia neta 
    '''
    profit_neto = (volume * final_price) - (volume * initial_price)
    return profit_neto

total_gain(12095.2, 0.86, 1.28)

ganancia_neta = total_gain(12095.2, 0.86, 1.28)

# Venta de items para comprar el libro

def compra_libro(initial_price, final_price, cost):
    '''
    -- Calcula ganancia por unindad
    
    -- Divide cost/ganancia por unidad --> cantidad de unidades necesarias para la compra
    '''
    
    profit_unitario = final_price - initial_price
    unidades_necesarias = cost / profit_unitario
    return print('Las unidades que se deben vender para cubrir la deuda y el costo del libro son: ' + str(unidades_necesarias) + ' GRO.')

compra_libro(0.86, 1.28, 2831.97)

   