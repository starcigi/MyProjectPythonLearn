class FileObject:
    def __init__(self,x = 'aaa.txt'):
        self.new_file = open(x,'r+')
    def __del__(self):
        self.new_file.close()
        del self.new_file   #删除文件
        print('调用中')
        
