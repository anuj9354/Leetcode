def reverse_32_bit(x: int) -> int:
    isNegative = False
    if x < 0:
        x , isNegative = -x , True        
    
    x = int(str(x)[::-1])
    if isNegative:
        if x > 2**31:
            return 0
        x = -x            
    elif x >= 2**31:
        return 0
        
    return x

num = int(input())
print (reverse_32_bit(num))
