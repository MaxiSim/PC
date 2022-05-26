'''
def list_remove(list_in, list_erase):
    result = []
    
    for value in list_in:
        if value not in list_erase:
            result.append(value)
       
    return result
    
list_remove([1,2,3,4,5,6,7], [4,5,6])

'''

def list_remove(list_in, list_erase):
    result = list_in[:]
    
    for value in list_erase:
        for i in list_in:
            if value == i:
                result.remove(value)
          
    print(result)
       
        
    
def main():
    list_in = [1,2,3,4,5,6,7] 
    list_erase = [4,5,6]
    list_remove(list_in, list_erase)
    

if __name__ == '__main__':
    main()