import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList,self).append(elem)
        self.log(elem)
