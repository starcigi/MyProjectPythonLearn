class Park():
    def __init__(self,child = False,weekend = False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.dis = 0.5
        else:
            self.dis = 1
    def add_price(self,num):
        return self.exp * self.inc * self.dis * num
        
        
