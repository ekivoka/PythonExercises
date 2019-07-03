class ExtendedStack(list):
    def sum(self):
        # операция сложения
        return self.append(self.pop()+self.pop())

    def sub(self):
        # операция вычитания
        return self.append(self.pop()-self.pop())

    def mul(self):
        # операция умножения
        return self.append(self.pop()*self.pop())

    def div(self):
        # операция целочисленного деления
        return self.append(self.pop()//self.pop())
