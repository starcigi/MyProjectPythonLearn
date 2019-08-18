alist = range(5)
it = iter(alist)

while True:
    try:
        print(next(it))
    except StopIteration:
        break
