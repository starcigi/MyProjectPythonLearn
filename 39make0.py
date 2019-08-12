class Turcle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x


class Pool:
    def __init__(self,x,y):
        self.turtle = Turcle(x)
        self.fish = Fish(y)
    def print_num(self):
        print('水池里总共有乌龟%d只，小鱼%d条！' % (self.turtle.num,self.fish.num))
        
class C:
    count = 0

    def __init__(self):
        C.count += 1
    def __del__(self):
        C.count -= 1
    
