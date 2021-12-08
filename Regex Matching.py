 def isMatch(self, s: str, p: str) -> bool:
    if not p:
        return not s
    
    firstMatch = len(s) > 0 and p[0] in {s[0], "."}
    if len(p) > 1 and p[1] == "*":
        return self.isMatch(s, p[2:]) or firstMatch or self.isMatch(s[1:], p)
    
    return firstMatch or self.isMatch(s[1:], p[1:])
