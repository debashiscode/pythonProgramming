# this is a single line comment
a = "this not a comment" #this is also comment
"""
This is multiline comment

"""
b =  """abc"""   # is this comment ?
print(a)
print(b)


x = None
if(x):
    print("True")
else:
    print("False")


#Boolean Operator


# bitwise operation

x = 3
print(x << 2)

# is equivalent to x * pow(2,2)

x = 3
print(x >> 2)

# is equivalent to x // pow(2, 2)



#Example-1
a = 10
b = 15
print(a & b )

#Example - 2
a = 10
b = 15
print(a | b)

#Example -3
a = 10
b = 15
a = a + (~b) + 1
print(a)

#Example -4
a = 5
b = 10
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print(a)
print(b)


a = [1,2,3]
for x in a:
    print(x)


for i in range(5):
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n // x}")
                break
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")




for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


while(True):
    print("loop continues until keyboard interrupt")
    pass


    break




def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 200:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


def func():
    print("Hello from function")

#calling function
func()


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))