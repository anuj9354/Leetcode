def titleToNumber(self, columnTitle: str) -> int:
    a , n = ord('A') - 1, 0
    for x in columnTitle:
        n = n*26 + ord(x) - a
    
    return n

s = input()
print (titleToNumber(s))
