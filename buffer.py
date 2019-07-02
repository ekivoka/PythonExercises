class Buffer:
    def __init__(self):
        self.buf = list()
        self.summa = 0
        self.c = 0
    
    def add(self, *a):
        for i in a:
            self.buf.append(i)
            self.summa += i
            self.c += 1
            if self.c == 5:
                print(self.summa)
                self.summa = 0
                self.c = 0
                self.buf = self.buf[5:]
        
    def get_current_part(self):
        return self.buf
