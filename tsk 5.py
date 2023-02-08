class student:

    def __init__(self,name,s1):
        self.name = name
        self.s1=s1
        
    def get_total(self):
        self.total = self.s1

    def get_percentage(self):
        self.get_total()
        self.per = self.total / 3

list_of_obj = []
for n in range(3):
    name = input("Enter your name: ")
    s1 = int(input("enter dsp marks "))
    
    st1 = student(name,s1)
    list_of_obj.append(st1)    

total = 0
for i in list_of_obj:
    i.get_total()
    print("the total is = ",i.total)
    i.get_percentage()
    print("per = ",i.per)
    total += i.s1
print("TOtal :", total)
