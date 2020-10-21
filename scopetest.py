def print_num():
    first_num = 1

    print("The first number is: ", first_num)
    print("===============Local scope function end==========")
print_num()

try:
    print("The first number defined is: ", first_num) # syntax error variable not declared ( value yra tik print_num() )
except:
    print("No number defined! (Attempted to access value first_num failed!)")

#Local scope end


greetings = "Hello"
def greet(name):
    print(greetings, name)
greet("World")
#Global scope end