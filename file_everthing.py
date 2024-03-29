def file_view(file_name,line_num):
    if line_num.strip() == ':':
        begin = '1'
        end = '-1'
    (begin,end) = line_num.split(':')

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'    #判断情况，立不同的标签，给前面无值和后面无值分别立标签

    if begin == '1' and end == '-1':
        prompt = '的全文'
    if begin == '1':
        prompt = '从开始到%s' % end
    if end == '-1':
        prompt = '从%s到借宿' % begin
    else:
        prompt = '从第%s行到第%s行' % (begin,end)  #利用上面的不同判断分别赋值

    print('\n文件%s%s的内容如下：\n' %(file_name,prompt))

    begin = int(begin) - 1
    end = int(end)
    lines = end - begin

    f = open(file_name)

    for i in range(begin):   #用于消耗begin之前的内容
        f.readline()


    if lines <  0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline, end='')

    f.close()

file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21: 或 : 】：')
file_view(file_name, line_num)

    
