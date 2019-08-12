def file_println(file,file_line):
    f = open(file)
    for i in range(int(file_line)):
        print(f.readline())
    f.close()

file = input('请输入需要打开的文件')
file_line = input('请输入需要显示该文件的前几行：')
file_println(file,file_line)
