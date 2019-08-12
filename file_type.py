import os
file_name = os.listdir('.')
txt = 0
png = 0
py = 0
docx = 0
file = 0
for each in file_name:
    if each.endswith('.txt'):
        txt += 1
    if each.endswith('.png'):
        png += 1
    if each.endswith('.py'):
        py += 1
    if each.endswith('.docx'):
        docx += 1
    if each.find('.') == -1:
        file += 1
print('该文件夹下共有类型为【.txt】的文件为%d个' % txt)
print('该文件夹下共有类型为【.png】的文件为%d个' % png)
print('该文件夹下共有类型为【.py】的文件为%d个' % py)
print('该文件夹下共有类型为【.docx】的文件为%d个' % docx)
print('该文件夹下共有类型为【文件夹】的文件为%d个' % file)
