
#%%
'''def rps (p1, p2):
    possibilities = ['scissors', 'paper', 'rock']
    import random
    
    for i in range(2):
        p1 = random.choice('scissors', 'paper', 'rock')
        p2 = random.choice('scissors', 'paper', 'rock')
        
        if p1 == p2 :
            return 'Draw'
        elif p1 == 'scissors' and p2 == 'paper':'''
    
#%%
def rps (p1, p2):
    possibilities = ['scissors', 'paper', 'rock']
    
    score_1 = 0 
    score_2 = 0 
    
    while score_1 < 2 or score_2 < 2:
        p1 = input("Ingrese opcion J1: ")
        p2 = input("Ingrese opcion J2: ")
        
        if (
            p1 == 'scissors' and p2 == 'paper' or
            p1 == 'paper' and p2 == 'rock' or
            p1 == 'rock' and p2 == 'scissors'
        ):
            score += 1
        
        elif p1 == p2:
            continue
        else:
            score_2 += 1
            
        if score_1 > score_2:
            return "Player 1 wins"
        else:
            return "Player 2 wins"
            
        
    return
    

def main():
    winner = rps()
    print(winner)
    
if __name__ == '__main__':
    main()
# %%
