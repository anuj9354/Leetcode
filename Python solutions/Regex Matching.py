def isMatch(text: str, pattern: str) -> bool:
    d , lp , lt = {} , len(pattern) , len(text)
    
    def topDownDP(i,j):
        if (i,j) not in d:
            if j == lp:
                ans = i == lt
            else:
                first_match = i < lt and pattern[j] in {text[i] , '.'}
                if j + 1 < lp and pattern[j + 1] == '*':
                    ans = topDownDP(i , j + 2) or first_match and topDownDP(i + 1 , j)
                else:
                    ans = first_match and topDownDP(i + 1 , j + 1)
                    
            d[i , j] = ans
        
        return d[i , j]
    
    return topDownDP(0 , 0) 

s , p = input().split(" ")
print (isMatch(s,p))
