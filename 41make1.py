class Cap(float):  #写类型
    def __new__(cls,x = 0.0):
        aaa = x*1.8 + 32
        return aaa.__new__(cls,aaa)
    
