def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0
    differ = []

    for each in f1:
        line2 = f2.readline()
        count += 1
        if each != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return(differ)

file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1,file2)

if len(differ) == 0:
    print('两个文件完全一样')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    for each in differ:
        print('第 %d 行不一样' % each)

