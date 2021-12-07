def Longest_Palindrome_Manacher(s):
    s1 , l = "|", len(s)
    l1 = l*2 + 1
    palinRadii = [0]*l1
    for i in range(l):
        s1 = s1 + s[i] + "|"

    center , radius = 0, 0
    while center < l1:
        while center - (radius + 1) >= 0 and center + (radius + 1) < l1 and s1[center - (radius + 1)] == s1[center + (radius + 1)]:
            radius += 1

        centerOld , radiusOld , palinRadii[center] = center , radius , radius
        center , radius = center + 1 , 0

        while center <= centerOld + radiusOld:
            # Because Center lies inside the old palindrome and every character inside a palindrome has a "mirrored" character reflected across its center, we
            # can use the data that was precomputed for the Center's mirrored point.
            mirrorCenter, maxMirrorRadius = centerOld + centerOld - center,  centerOld + radiusOld - center
            
            if palinRadii[mirrorCenter] < maxMirrorRadius :
                palinRadii[center] = palinRadii[mirrorCenter]
                center += 1
            elif palinRadii[mirrorCenter] > maxMirrorRadius:
                palinRadii[center] = maxMirrorRadius
                center += 1
            else:
                radius = maxMirrorRadius
                break

    maxi , pos = 0 , 0
    for i in range(l1):
        if palinRadii[i] > maxi:
            maxi = palinRadii[i]
            pos = i

    i , j , ans = pos - maxi , pos + maxi, ""
    while i < j:
        if s1[i] != "|":
            ans += s1[i]
        i+=1

    return ans

def Longest_Palindrome_Slow(s):
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
print (Longest_Palindrome_Manacher(s))
        
