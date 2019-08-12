import easygui as g
import sys

while 1:
    g.msgbox("嗨！欢迎进入第一个界面小游戏~")

    msg = "请问你想学什么呢？"
    title = "小游戏互动"
    choices  = ["谈恋爱","编程","OOXX","琴棋书画"]

    choice = g.choicebox(msg,title,choices)

    #注意，msgbox的参数是一个字符串
    #如果用户选择Cancel,该函数返回None
    g.msgbox("你的选择是：" + str(choice), "结果")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    #弹出一个Coninue/Cancel对话框
    if g.ccbox(msg,title):
        pass           #如果用户选择Continue
    else:
        sys.exit(0)     
