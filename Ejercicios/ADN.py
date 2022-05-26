
def compress (strand: str) -> str:
    counter = 1
    result = []
    current = strand[0]
    
    for i in range (1, len(strand), +1):
    
        if i < len(strand):
            if strand[i] == current:
                counter += 1
                continue 
        
        if counter == 1:
            result.append(current)
        else:
            result.append(str(counter))
            result.append(current)
            counter = 1
    
        if i < len(strand):
            current = strand[i]
            
       
            
    return ''.join(result)
    
        
    

    
    
compress('AACGGGGGTTTAACCGTT')