def func(n):
    print(n)
    if n == 1:
        return n
    elif n % 2 == 1:
        return func((3 * n) + 1)
    else:
        return func(int(n / 2))

func(3)

def func2(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    return func2(data - 1) + func2(data - 2) + func2(data - 3)

print(func2(4))