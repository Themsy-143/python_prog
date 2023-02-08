class bottle:
    def __init__(self,name,bottle_cap,colour):
        self.name = name
        self.bottle_cap = bottle_cap
        self.colour = colour
    
    def __str__(self):
        return f"{self.name} {self.bottle_cap} {self.colour}"

lst = []
for i in range(2):
    nme = input("Enter the name of bottle: ")
    bt_cp = float(input("enter size of bottle cap: "))
    clr = input("Enter colour of the bottle: ")
    s = bottle(nme,bt_cp,clr)
    lst.append(s)

for j in lst:
    print(j)
  

print("commit test")