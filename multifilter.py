class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos>=neg:
            return True
        return False
    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos>0:
            return True
        return False
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        return False
    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        # funcs - допускающие функции
        # judge - решающая функция
    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        self.n = 0
        return self
    def __next__(self):
        if self.n<len(self.iterable):
            elem = self.iterable[self.n]
            self.n += 1
            if self.is_appropriate(elem):
                return elem
            else:
                return(self.__next__())
                
        else:
            raise StopIteration
    def is_appropriate(self,elem):
        neg = 0
        pos = 0
        
        for f in self.funcs:
            if f(elem):
                pos += 1
            else:
                neg += 1
        if self.judge(pos, neg):
            return True
        return False
            
        
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]
b = list(multifilter(a, mul2, mul3, mul5))
