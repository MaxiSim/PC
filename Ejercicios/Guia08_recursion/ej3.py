
def rev(x, prod=0):
    if x < 10:
        return prod + x
    else:
        prod = prod * 10 + x%10 * 10
        return rev(x // 10, prod)
    
