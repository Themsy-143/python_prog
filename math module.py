import math
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = input("what do you want to do with this no.: add = a\n subtract = s\n multiply = m\n divide = d\n power = p\n square root = sr\n")

if c == "a":
    d = int(a) + int(b)
    print(d)

elif c== "s":
    e = int(a) - int(b)
    print(e)

elif c == "m":
    f = int(a) * int(b)
    print(f)
    
elif c == "d":
    if int(a) == 0 or int(b) == 0:
        print("choose other number")
    else:
        g = int(a) / int(b)
        print(g)

elif c == "p":
    h = pow(a,b)
    print(h)

elif c == "sr":
    i = math.sqrt(a)
    print(i)

else:
    print("wrong choice")