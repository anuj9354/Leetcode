def convertToTitle(self, n: int) -> str:
    s , a = "", ord('A') - 1
    while n > 0:
        x = n%26
        if x:
            s += chr(a + n%26)
            n//=26
        else:
            s , n = s + 'Z' , n//26 - 1
            if n == 0:
                break
                
    return s[::-1]

columnNumber = int(input())
print (convertToTitle(columnNumber))
