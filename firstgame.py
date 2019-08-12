import random
secret = random.randint(1,5)
print('----first game----')
temp = input('猜我心中的数字')
guess = int(temp)
num = 3
if guess == secret:
    print('一次猜中！真厉害~')
else:
    while guess != secret and num != 0:
        temp = input('猜错了，请重新输入')
        guess = int(temp)
        if guess == secret:
            print('猜对啦')
        else:
                if guess > secret:
                        print('大了')
                        num = num - 1
                else:
                        print('小了')
                        num = num - 1
                if num > 0:
                        print('again')
                else:
                        print('over')
    print('游戏结束')
