def binhanshu(x):
    result = ''
    if x:
        result = binhanshu(x//2)
        return result + str(x%2)
    else:
        return result
