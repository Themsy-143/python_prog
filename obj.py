class student:

    def __init__(self,name,s1,s2,s3):
        self.name = name
        self.s1=s1
        self.s2=s2
        self.s3=s3

    def get_total(self):
        self.total = self.s1+self.s2+self.s3
        
    def get_percentage(self):
        self.get_total()
        self.per = self.total / 3

list_of_obj = []
for n in range(3):
    name = input("Enter your name: ")
    s1 = int(input("enter dsp marks "))
    s2 = int(input("Enter AI marks: "))
    s3 = int(input("Enter IOT marks: "))
    st1 = student(name,s1,s2,s3)
    list_of_obj.append(st1)    

for i in list_of_obj:
    i.get_total()
    print("the total is = ",i.total)
    i.get_percentage()
    print("per = ",i.per)

