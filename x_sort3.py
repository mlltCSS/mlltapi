def mysort(args):
    x = len(args)
    for y in range(x - 1):
        for z in range(0, x - y - 1):
            if args[z] > args[z + 1]:
                args[z], args[z + 1] = args[z + 1], args[z]
    return args

x = [0]*10
y = 0
while y < 10:
    print("Please enter x",y+1," value.")
    x[y] = int(input())
    y = y + 1
mysort(x)
print("Final result:", x)





