lins = []
def get_digits(x):
    if x > 0:
       lins.insert(0,x%10)
       get_digits(x//10)
print(lins)
