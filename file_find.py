import os

def file_find(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir): #列举目录中的文件名
        if each_file == target:
            print(os.getcwd() + os.sep + each_file) #使用os.sep使程序更标准
        if os.path.isdir(each_file):#判断置顶路径是否存在且是一个目录（文本文件）
            file_find(each_file,target)  #递归调用
            os.chdir(os.pardir) #递归调用后返回上一层目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入需要查询的文件：')
file_find(start_dir,target)
        
        

    
