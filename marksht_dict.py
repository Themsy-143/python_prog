class Marksheet:
    def info(a, b, c):

       
        l = dict{"name":a, "total":b, "percentage":c}
        print(l)
        if sub1m <= 60:
            print("your DSP mks are less than 60 ")
        elif sub2m <= 60:
            print("your AI mks are less than 60 ")
        elif sub3m <= 60:
            print("your IOT mks are less than 60 ")
        else:
            print("Congrats! you've cleared the exam ")
        
        def sl():
            print(l)

            
n = int(input("Enter number of student: "))
for s in range(0, n):
    name = input("Enter your name: ")
    sub1m = int(input("Enter DSP marks: "))
    sub2m = int(input("Enter AI marks: "))
    sub3m = int(input("Enter IOT marks: "))
    total = sub1m + sub2m + sub3m
    percentage = (total / 300)*100
    s = Marksheet()
    s.info(name,total,percentage)

s2 = Marksheet()
s2.sl()






    

