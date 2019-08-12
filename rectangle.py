class Rectangle():
    height = 5.00
    width = 4.00
    def setRect(self):
        print('请输入长和宽')
        a = int(input('长：'))
        b = int(input('宽：'))
        self.height = a
        self.width = b
    def getRect(self):
        print('这个矩形的长是：%d,宽是%d' % (self.height,self.width))
    def getArea(self):
        c = self.height * self.width
        print(c)
