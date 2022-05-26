def generateRange(min: int, max: int, step: int) -> None:
    for i in range(min, max +1, step):
        print(i)    

def main():
    generateRange(2,10,2)
    
if __name__ == '__main__':
    main()
    
    
#%%
    
def generate_range(min: int, max: int, step: int) -> None:
        
    i = min
        
    while i <= max:
        print(i)
            
        i += step

generate_range(2,10,2)


# %%
