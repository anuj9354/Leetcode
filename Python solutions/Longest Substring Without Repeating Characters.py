def lengthOfLongestSubstring(self, s: str) -> int:
    i , l , maxi, current, start = 0 , len(s), 0 , 0, 0
    pos, val = [-1]*256, [-1]*l
    
    while i<l:
        val[i] = ord(s[i])
        if pos[val[i]] > -1:
            if maxi < current:
                maxi = current
            
            current = current - pos[val[i]] + start
            while start < pos[val[i]]:
                pos[val[start]] = -1
                start += 1
            start += 1                               
        else:
            current += 1
        pos[val[i]] = i
        i+=1
    
    if maxi < current:
        return current
    return maxi

s = input()
print (lengthOfLongestSubstring(s))
