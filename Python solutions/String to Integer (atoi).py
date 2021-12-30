def customAtoi(s: str) -> int:
    i , l , ans , power = 0 , len(s), 0 , 2**31
    while i<l and s[i] == " ":
        i+=1
    
    if i<l:
        zero , isNegative =  ord("0") , False
        if s[i] == "-":
            i , isNegative = i + 1 , True
        elif s[i] == "+":
            i+=1

        while i<l and s[i] >= "0" and s[i] <= "9":
            ans = ans*10 + ord(s[i]) - zero
            i+=1
    
        if isNegative:
            if ans <= power:
                return -ans
            return -power
    
    if ans < power:
        return ans    
    return power - 1

x = input()
print (customAtoi(x))


