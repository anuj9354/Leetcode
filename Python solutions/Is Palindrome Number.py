def isPalindrome(self, x: int) -> bool:
    if x < 0 || (x%10 == 0 and x != 0):
        return False

    reversedNum = 0
    while x > reversedNum:
        reversedNum = reversedNum * 10 + x%10
        x //= 10   
    
    return x == reversedNum || x == reversedNum //10

n = int(input())
print (isPalindrome(n))
