class Marksheet:
    def __init__ (self,name,s1,s2,s3,total,percentage):
        self.name = name
        self.s1= s1
        self.s2=s2
        self.s3=s3
        self.total= total
        self.percentage = percentage

    def all_tot(self):
        return self.total

    def all_per(self):
        return self.percentage
    
    def sub_1(self):
        return self.s1,
    def sub_2(self):
        return self.s2,
    def sub_3(self):
        return self.s3

    def nme(self):
        return self.name

name = input("Enter your name: ")
s1m = int(input("Enter DSP marks: "))
s2m = int(input("Enter AI marks: "))
s3m = int(input("Enter IOT marks: "))
tot = s1m + s2m + s3m
per = (tot / 300)*100
       
s=Marksheet()
print(s.all_tot)
print(s.all_per)
print(s.all_mks)
print(s.nme)
