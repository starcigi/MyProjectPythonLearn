class Nstr(str):
    def __sub__(self,other):
        return self.replace(other,'')   #替换字符串
    
