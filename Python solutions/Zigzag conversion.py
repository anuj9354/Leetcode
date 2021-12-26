def convert(s: str, numRows: int):
    if numRows == 1:
        return s
    else:
        arr, i , j , l , y = [""]*numRows, 0, 0, len(s), numRows - 1
        
        while i < l:
            if j == 0:
                x = 0
                while i<l and x < numRows:
                    arr[x] += s[i]
                    x , i = x + 1, i + 1
            else:
                arr[numRows - j - 1] += s[i]
                i+=1
            j = (j + 1) % y
        return "".join(arr)

s1 = input()
n = int(input())
print (convert(s1,n))
        
        

    
    
