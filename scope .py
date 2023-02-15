#function()
  
def dosmthng(b):
    if int(b) <=20:
        print("student")
    else:
        print("bchlor")

def function_one():
    for i in range(0,3):
        a = input("Enter your Name: ")
        print(a)
        b = input("Enter your age: ")
        dosmthng(b)
    print("Ok Byy!!")

function_one()

#=========================================================

def rnge(ar):
    i = 1
    if ar == "even":
        while i <= 50:
            if i % 2 == 0:
                print(i)
            i+=1
    elif ar =="odd":
        while i <= 50:
            if i % 2 != 0:
                print(i)
            i+=1

def dsa():
    a = input("Enter your choice:(even/odd)")
    print(a)

    rnge(a)

dsa()



