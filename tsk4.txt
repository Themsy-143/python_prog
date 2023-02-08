# Recursion
def tri_recursion(k):
    l = 2 
    if(k > 0):

        result = l * tri_recursion(k-1)
        print(result)
    else:  
        print()
        result = 4
    return result

print("\nRecursion Example Results")
tri_recursion(6)

#class/object

class nwcls:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def fnc(self):
        print("My name is " + self.name + " " + "My age is " + self.age)
    # def function_1(self):
        # print("my name is " + self.name)
    
p1 = nwcls ("Themsy" , "20")
p1.fnc()
del p1.name
p1.name = "Bhavi"
print(p1.name)

