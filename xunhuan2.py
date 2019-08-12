print('============RESTART=============')
num = input('请输入一个整数：')
star = int(num)
while star:
    i = star - 1
    while i:
        print(' ', end = '')
        i = i - 1
    j = star
    while j:
        print('*', end = '')
        j = j - 1
    print()
    star = star -1
    
