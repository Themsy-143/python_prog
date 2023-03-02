h = eval(input("Enter triangle's height: "))

for i in range(h):
    for j in range(i + 1):
        print(" * ", end="")
    print()
for i in range(h):
    for j in range(h - i - 1):
        print(" * ", end="")
    print()
