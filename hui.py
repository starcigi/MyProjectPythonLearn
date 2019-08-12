def gun(hui):
    length = len(hui)
    for each1 in range(length - 1):
        a = length
        if hui[a - length] == hui[length - 1]:
            length -= length
        else:
             print('不是回文联')
             break
        print('是回文联')

hui = input('请输入一句话：')
gun(hui)
