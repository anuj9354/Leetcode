def isStringDecomposable(s:str) -> bool:
    l , i , arr , exact = len(s) , 0 , [] , 0
    while i < l:
        x , count = s[i] , 1
        i+=1
        while i < l and s[i] == x:
            i , count = i + 1, count + 1
        if count % 3 == 0:
            continue
        elif count % 3 == 2 and exact == 0:
            exact += 1
        else:
            return False       
        
    return exact == 1

s = input()
print (isStringDecomposable(s))
