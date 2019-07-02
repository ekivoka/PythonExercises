class MoneyBox:
    def __init__(self, capacity=0):
        self.capacity = capacity
    def can_add(self, v):
        if self.capacity>=v:
            return True
        return False
    
    def add(self,v):
        if can_add(self, v):
            self.capacity -= v
        
