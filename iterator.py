from random import random

class RandomIterator:
    def __iter__(self):
        return(self)
    def __init__(self,n):
        self.n = n
    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return random()
        else:
            raise StopIteration
       
x = RandomIterator(5)
for i in x:
    print(i)
