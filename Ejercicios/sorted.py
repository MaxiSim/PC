
letras = [('a', 0.2),('b', 0.01),('c',3)]
ordenada = sorted(letras, key = lambda par: par[1])

print (ordenada)

#%%
letras = [('a', 0.2),('b', 0.01),('c',3)]
def por_valor(par):
    return par[1]

ordenada = sorted(letras, key = por_valor)
print(ordenada)


