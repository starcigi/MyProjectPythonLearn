class Fibs:
    def __init__(self,n = 10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self   #因为它本身就是一个迭代器
    def __next__(self):
        self.a,self.b= self.b,self.a+self.b
        if self.a >self.n:
            raise StopIteration
        return self.a
