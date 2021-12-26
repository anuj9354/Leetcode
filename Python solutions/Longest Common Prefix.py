def longestCommonPrefix(strs) -> str:
    s , j , count , ls , done = "" , 0 , len(strs), [] , False

    for x in strs:
        ls.append(len(x))
    
    while ls[0] > j:
        x , i = strs[0][j] , 1
        
        while i < count:
            if ls[i] > j and strs[i][j] == x:
                i+=1                                
            else:
                done = True
                break
        if done:
            break
        else:
            s , j = s + x , j + 1

    return s

arr = input().split(" ")
print (longestCommonPrefix(arr))
