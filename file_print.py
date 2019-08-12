file_name = input('请输入文件名：')
file_words = input('请输入内容：【单独输入‘:w’保存并退出：】')
file_true = input()
length = len(file_words)

f = open(file_name,'w')
if (file_true == ':w'):
    f.write(file_words)
    f.close()
