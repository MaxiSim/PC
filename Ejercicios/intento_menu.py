
def ir_izquierda():
    print('izquierda')
def ir_derecha():
    print('derecha')
def ir_arriba():
    print('arriba')
def ir_abajo():
    print('abajo')
def menu(prompt: str, opciones: list) -> str :
    print(prompt)
    for i, opcion in enumerate(opciones):
       print(f'{i + 1}. {opcion}')
  
    return opciones[int(input("> ")) - 1]             


movimientos = {
    'izquierda': ir_izquierda,
    'derecha': ir_derecha, 
    'arriba': ir_arriba, 
    'abajo': ir_abajo
}

move = menu("Hacia donde queres ir?", list(movimientos.keys()))
movimientos[move]()