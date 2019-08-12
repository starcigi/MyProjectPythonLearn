import os
file_name = os.listdir('.')
for each in file_name:
    size = os.path.getsize(each)
    print(each,size)
