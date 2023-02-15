class M_Category:
    def __init__(self,c_id,c_name,c_price):
        self.c_id = c_id
        self.c_name = c_name
        self.c_price = c_price
    
    def print_para(self):
        print(self.c_id,self.c_name,self.c_price)

class M_Product(M_Category):
    def __init__(self,p_id,p_name,price):

        super().__init__(c_id=p_id,c_name=p_name,c_price=price)
    
    def print_paras(self):
        M_Category.print_para(self)
        # print(self.p_id,self.p_name,self.p_cate,self.price)




def ad_ct(): 
    x = 'y'
    while x == 'y':
        c_id = int(input("Enter category ID :"))
        c_name = input("Enter category Name :")
        c_price = float(input("Enter price of category: "))
        obj = M_Category(c_id,c_name,c_price)
        category.append(obj)
        x = input("do you want to add another category? (y/n) :")

def display():
    for i in category:
        i.print_para()

def ad_pr():
    x = 'y'
    while x == 'y':
        p_id = int(input("Enter product ID :"))
        p_name = input("Enter product Name :")
        price = float(input("Enter price of the product: "))
        print()
        obj1 = M_Product(p_id,p_name,price)
        product.append(obj1)
        x = input("do you want to add another product? (y/n) :")

def display_p():
    for i in product:
        i.print_paras()

category = []
product = []

while True:
    choice = input("What do you want to do?:\n add = A display = D\n")
    match choice:  
        case 'A':
                ask = input("What do you want to add: Category = c\n, product = p\n")

                if (ask == 'c'):
                    ad_ct()
                    display()
                elif (ask == 'p'):
                    ad_pr()
                    display_p()

        case 'D':
                ask = input("What do you want to display: Category = c\n, product = p\n ")
                
                if (ask == 'c'):
                    display()
                elif(ask == 'p'):
                    display_p()

        case _:
            print("WRONG CHOICE")
            break


