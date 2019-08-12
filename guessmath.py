import random
import easygui as g
secret = random.randint(1,5)
print('----first game----')
temp = g.integerbox('猜我心中的数字')
guess = int(temp)
num = 3
if guess == secret:
    g.msgbox('一次猜中！真厉害~')
else:
    while guess != secret and num != 0:
        temp = g.integerbox('猜错了，请重新输入')
        guess = int(temp)
        if guess == secret:
            g.msgbox('猜对啦')
        else:
                if guess > secret:
                        g.msgbox('大了')
                        num = num - 1
                else:
                        g.msgbox('小了')
                        num = num - 1
                if num > 0:
                        g.msgbox('again')
                else:
                        g.msgbox('over')
    g.msgbox('游戏结束')
