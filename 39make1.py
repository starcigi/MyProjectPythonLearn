#一个栈类（stack），用来模拟后进先出（LIFO）特性的数据结构。需要以下方法
#isEmpty()  判断当前栈是否为空
#>>> not True  False>>> not False  True
#push() 往栈的顶部压入一个数据项
#pop() 从栈顶弹出一个数据项（并在栈中删除）
#top() 显示当前栈项的一个数据项
#bottom() 显示当前栈底的一个数据项
class Stack:
    def __init__(self,start = []):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):
        return not self.stack    #return not 返回布尔类型值  

    def push(self):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]
