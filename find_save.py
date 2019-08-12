import os

def search_file(start_dir,target):
    os.chdir(start_dir)

    for each in os.listdir(os.curdir):
        ext = os.path.splitext(each)[1]
        if ext in target:
            vedion_list.append(os.getcwd() +os.sep + each +os.linesep)
        if os.path.isdir(each):
            search_file(each,target)
            os.chdir(os.pardir)
start_dir = input('请输入需要查到的目录')
program_dir = os.getcwd()

target = ['.mp4','.avi','.rmvh']
vedio_list = []

search_file(start_dir,target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
