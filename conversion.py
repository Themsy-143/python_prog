list = []

n = int(input("How many items you want: "))

for i in range(0,n):
    dict = {
        "a" : input("Enter Item: "),
        "b" : float(input("Enter weight of 1 item in kgs: ")),
        "c" : float(input("Enter weightof item you have kgs: "))
        }
    list.append(dict)
print(list)

for j in list:
    d = j['c']/(j['b'])
    print(str(d)+" nos. of " + j['a'] + " we have")
