def libs():    #斐波那契数列的生成器输出
    a = 0
    b = 1
    while True:
        a,b = b, a+b
        yield a

#for each in libs():
	#if each > 100:
		#break
	#print(each)
