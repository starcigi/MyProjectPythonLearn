class Fish:
    def __init__(self,x):
        self.shu = x
class Turble:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.fish = Fish(x)
        self.turble = Turble(y)
    def print_one(self):
        print('一共有鱼%d条，乌龟%d只' % (self.fish.shu,self.turble.num))
