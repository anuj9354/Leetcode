from collections import defaultdict

class Solution:
    def __init__(self):
        self.dictCode = defaultdict(list)
        self.dictCode["2"] = ["a", "b", "c"]
        self.dictCode["3"] = ["d", "e", "f"]
        self.dictCode["4"] = ["g", "h", "i"]
        self.dictCode["5"] = ["j", "k", "l"]
        self.dictCode["6"] = ["m", "n", "o"]
        self.dictCode["7"] = ["p", "q", "r", "s"]
        self.dictCode["8"] = ["t", "u", "v"]
        self.dictCode["9"] = ["w", "x", "y", "z"]
        
    def addDigitToCombinations(self, digits: str, index:int, length: int, arr: List[str]) -> List[str]:
        if index == length:
            return arr
        
        dataSet = []
        for x in arr:
            for y in self.dictCode[digits[index]]:
                dataSet.append(x+y)
                
        return self.addDigitToCombinations(digits, index + 1, length, dataSet)        
    
    def letterCombinations(self, digits: str) -> List[str]:
        l = len(digits)
        
        if l == 0:
            return []
        elif l == 1:
            return self.dictCode[digits[0]]
        else:
            return self.addDigitToCombinations( digits, 1, l, self.dictCode[digits[0]] )
        
        
