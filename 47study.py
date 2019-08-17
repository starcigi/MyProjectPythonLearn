class Listow:
    def __init__(self,*args):  #可变数量
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0) #创建长度为len的整数列表  用于查访问次数时使用
    def __len__(self):
        return len(self,values)
    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]
            
