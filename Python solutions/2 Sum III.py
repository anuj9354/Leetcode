class TwoSum:
    obj = {} 
    def __init__(self):
        self.obj = {}
        return None
        
    def add(self, number: int) -> None:
        if number in self.obj:
            self.obj[number] += 1
        else:
            self.obj[number] = 1

        return None
        
    def find(self, value: int) -> bool:
        for x in self.obj.keys():
            if value - x in self.obj and (x != value - x or self.obj[x] > 1):
                return True
        
        return False

obj = TwoSum()
obj.add(number)
param_2 = obj.find(value)
