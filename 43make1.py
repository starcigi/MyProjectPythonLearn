class Word(str):
    def __new__(cls,word):
        #str是不可变的类型，所以必须使用new
        #创建她的时候初始化
        if ' ' in word:
            print ("Value contains spaces.Truncating to first space")
            word = word[:word.index(' ')] #单词是第一个空格之前所有的字符
        return str.__new__(cls,word)

    def __gt__(self,other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
