x = [None]*10
y = 0
while y < 10:
    print("Please enter x",y+1," value.")
    x[y] = input()
    y = y + 1
#Integer sort
x.sort(key=int)
print("Final result:", x)





