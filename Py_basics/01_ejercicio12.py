#Juntada de gpo


def main(cant_gente, pizza_6, pizza_8, postre, bebida_picada):
    '''
    - Calcular cantidad de porciones de pizza
    -  Calcular precio de las pizzas
    - Calcular costo total
    - Calcular promdedio a pagar x c/u
    
    '''
    cant_pizzas = cant_gente * 4 / 6
    precio_pizza = cant_pizzas * pizza_6
    costo_total = precio_pizza + postre + bebida_picada
    promedio = costo_total / 5
    
    
    
    print('Costo total: $' + str(costo_total))
    print('Promedio a pagar por persona: $' + str(promedio))  

main(5, 1020, 800, 410)

 
