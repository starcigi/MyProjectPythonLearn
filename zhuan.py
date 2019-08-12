print('===========RESTART==============')
q = True
while q:
    first = input('请输入一个整数（输入q结束程序）：')
    if first != 'Q':
        first = int(first)
        print('%#o' % first),
        print('%#x' % first),
        print(bin(first)),
    else:
        q = False
        
