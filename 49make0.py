def myRev(a):
    x = str(a)
    length = len(x) - 1
    while True:
        if length > -1:
            yield x[length]
        length -= 1

        
    
