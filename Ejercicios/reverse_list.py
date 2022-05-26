
def reverse_list(list):
    output = []
    for i in range(len(list)-1,-1,-1):
        output.append(list[i])
    return output   
    
def reverse_optimized(list):
    left = 0
    right = len(list)-1
    
    while left < right:
        aux = list[right]
        list[right] = list [left]
        list[left] = aux
        
        left += 1
        right -+ 1
    
    return list
        

def main():
    list = [1,2,3,4]
    output = reverse_optimized(list)
    print(output)
    
if __name__ == '__main__':
    main()