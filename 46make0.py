class MyDes:
    def __init__(self,initval = None,name =None):
        self.val = initval
        self.name = name
    def __get__(self,instance,owner):
        print('正在获取变量：',self.name)
        return self.val
    def __set__(self,instance,value):
        print('正在修改变量：',self.name)
        self.val = value
    def __delete__(self,instance):
        print('正在删除变量：',self.name)
        print('哦这个变量没法儿删除')     #这里描述符起到的作用是间接地保存指定变量的数据
