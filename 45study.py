class Rectangle:
    def __init__(self,width = 0,height = 0):
        self.width = width
        self.height = height
    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name,value)  #self.__dict__[name] =value 以字典的形式传值
    def getArea(self):
        return self.width * self.height
  
