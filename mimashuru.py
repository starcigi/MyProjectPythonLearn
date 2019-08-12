print('===========RESTART========')
c = 3
while c:
    a = input('请输入密码：')
    b = 'FishC.com'
    if '*' in  a:
        print('密码中不能含有“*”号！您还有三次机会！')
        continue
    elif b != a:
        print('密码输入错误！',c,'您还有''次机会!')
        c = c -1
    elif b == a:
        print('密码正确，进入程序...')
