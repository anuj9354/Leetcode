def LCS_Slow(s):
    s1 , l = "|", len(s)
    l1 = l*2 + 1
    palinRadii = [0]*l1
    for i in range(l):
        s1 = s1 + s[i] + "|"

    center = 0
    while center < l1:
        radius = 0

        while center - (radius + 1) >= 0 and center + (radius + 1) < l1 and s1[center - (radius + 1)] == s1[center + (radius + 1)]:
            radius += 1

        palinRadii[center] = radius
        center+=1

    maxi = max(palinRadii)

    return maxi

s = input()
print (LCS_Slow(s))
        
