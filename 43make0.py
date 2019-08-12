class Guess:
    def __init__(self,*arg):  #星号代表多个参数
        if arg == 0:
            print('并没有传入参数')
        else:
            print("传入了 %d 个参数，分别是：" % len(arg))
            for each in arg:
                print(each)
        
