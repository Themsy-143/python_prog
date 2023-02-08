#add elements of list a to b
#addition of all the elements in a
a=[1,2,3,4,5,4,2,6,5,8,7,5]
b = 0
# a.append(b)
# print(a)
for i in a:
    # b.append(i)
    b = b+i
print(b)

#calc. using function
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("what do you want to do with this no.:(add/sub/mul/div)")

def add(a,b):
    print("the addition is = ", a+b)
def sub(a,b):
    print("the subtraction is = ", a-b)
def mul(a,b):
        print("the multiplacation is =",a*b)
def div(a,b):
    print("the division is =",a/b)

if c == "add":
    add(int(a),int(b))
if c == "sub":
    sub(int(a),int(b))
if c == "mul":
    mul(int(a),int(b))
if c == "div":
    if (int(a)==0 or int(b)==0):
        print("choose other number")
    else:
         div(int(a),int(b))
