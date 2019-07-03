class Buffer:
    def __init__(self):
        self.buf = list()

    def add(self, *a):
        self.buf += a
        for i in range(len(self.buf)//5):
            print(sum(self.buf[:5]))
            self.buf=self.buf[5:]
                
    def get_current_part(self):
        return self.buf