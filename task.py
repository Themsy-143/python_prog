class bottles:
    def __init__(self,type,ltrs):
        self.type = type
        self.ltrs = ltrs

    def get_bottle(self):

        if self.ltrs<=20:
            if (self.ltrs>=1 and self.ltrs<=2.5):
                print(" normal bottle")
            elif (self.ltrs>=2.6 and self.ltrs<=10):
                print("big bottle")
            elif (self.ltrs>10 and self.ltrs<=15):
                while True:
                    c = input("do you want TAP: y/n ")
                    if (c == 'y'):
                        print("Filter")
                        break
                    else:
                        print("l_bottle")
                    break
            elif (self.ltrs>15):
                print("t_bottle")
        else:
            print("We dont provide barls")

type= input("Which type of bottle you want:  ")
ltrs = float(input("How many litres of bottle you want:  "))

ob = bottles(type,ltrs)
ob.get_bottle()

print()
