

def rec_sum1(z,k):
    res = 0
    if k == 0:
        return z
    else:
        res = z + 1
    return rec_sum1(res,k-1)

# print(rec_func(4,6))

def rec_mult_sumsus (z,k):
    res = 0 
    if k == 0:
        return 0
    if k == 1:
        return z
    else:
        res += z
    return res + rec_mult_sumsus(z,k-1) 

# print(rec_mult_sumsus(2,4))

def rec_pot_multsus(z,k):
    res = z
    if k == 0:
        return 1
    if k == 1:
        return z
    
    return res * rec_pot_multsus(z,k-1)

# print(rec_pot_multsus(3,3))
#%%

def digit_count(num, digits = 0) -> int:
    if num == 0:
        if digits != 0:
            return digits
        else:
            return 1
    else:
        return digit_count(num // 10, digits +1)
# print(digit_count(128))

#%%
def rev(x, prod=0):
    if x < 10:
        return prod + x
    else:
        prod = prod * 10 + x%10 * 10
        return rev(x // 10, prod)
    

#%%
def fact(n: int, contador = 1) -> int:
    res = 0
    if n == 0 or n == 1:
        return n 
    else:
        if contador == n:
            return res + n
        else:
             res += contador
        return res + fact(n, contador+1)
    
# print(fact(4))
# %%
def valid(n,b)-> bool:
    if n == b:
        return True
    elif n < b:
        return False
    return valid(n/b,b)
    
# print(valid(16,4))

#%%
def largest(vector: list):
    if len(vector)==1:
        return vector[0]
    else:
        if vector[0]>=vector[1]:
            vector.remove(vector[1])
        else:
            vector.remove(vector[0])
        return largest(vector)
    
# print(largest([1,4,3,7])) 

#%%
fib_calls = 0
def fib(n):
    global fib_calls
    fib_calls += 1

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
    
# print(fib(6), fib_calls)

#%%
def mcd(x,y):
    if x == y:
        return x 
    elif x == 0:
        return y
    elif y == 0:
        return x
    if x > y:
        return mcd(x-y,y)
    elif x < y:
        return mcd(x, y-x)
    
# print (mcd(8,20))

#%%
def maxval(x: list) -> int:
    if len(x) == 1:
        return x
    else:
        if x[0] > x[1]:
            x.remove(x[1])
        else:
            x.remove(x[0])
        return maxval(x)
    
# print(maxval([1,8,4,3,10]))

#%%
def pascal(n,k):
    if n >= 0:
        if k == 0 or k == n:
            return 1
        else:
            return pascal(n-1, k-1) + pascal(n-1,k)

# print(pascal(6,2))

#%%
import random
from re import S
def tenis(j1=0,j2=0):
    jugadores = [1,2]
    ganador = random.choice(jugadores)
    if ganador == 1 and j1 == 0:
        return tenis(j1+15, j2)
    if ganador == 1 and j1 == 15:
        return tenis(j1+15, j2)
    if ganador == 1 and j1 == 30:
        return tenis(j1+10, j2)
    if ganador == 1 and j1 == 40 and j2<j1:
        return j1+20, j2
    if ganador == 1 and j1 == 40 and j2 == 40:
        return tenis(j1+10, j2)
    if ganador == 1 and j1 == 50 and j2 == 40:
        return j1+10, j2
    
    if ganador == 2 and j2 == 0:
        return tenis(j1, j2+15)
    if ganador == 2 and j2 == 15:
        return tenis(j1, j2+15)
    if ganador == 2 and j2 == 30:
        return tenis(j1, j2+10)
    if ganador == 2 and j2 == 40 and j1<j2:
        return j1, j2+20
    if ganador == 2 and j2 == 40 and j1 == 40:
        return tenis(j1, j2+10)
    if ganador == 2 and j2 == 50 and j1 == 40:
        return j1, j2+10
    
    if ganador == j2 and j2 == 40 and j1 == 50:
        return tenis(j1-10, j2)
    if ganador == j1 and j1 == 40 and j2 == 50:
        return tenis(j1, j2-10)
 
# print(tenis())   

#%%
def f(n):
    """
    The f function returns the string representation of an integer, n.
    If the length of that string is less than or equal to 1, it returns that string.
    Otherwise it returns a concatenation of strings: f(n-3) + f(n-2) + f(n-2).
    
    
    :param n: Store the current number being iterated over
    :return: The string representation of the integer n
    :doc-author: Trelent
    """
    s = str(n)
    
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

# print(f(543))

#%%
def g(x):
    return h(str(x))

def h(x):
    '''
    Devuelve la suma de los digitos de x.
    '''
    if len(x) == 1:
        return int(x)
    
    n = int(x[0]) + int(x[1])
    
    if len(x) == 2:
        return n
    else:
        return n + h(x[2:])    
    
print(g(2112))