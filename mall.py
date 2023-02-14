class M_Category:
    def __init__(self,c_id,c_name):
        self.c_id = c_id
        self.c_name = c_name

    def print_para(self):
        print(self.c_id,self.c_name)
        
def ad_ct(): 
    x = 'y'
    while x == 'y':
        c_id = int(input("Enter category ID :"))
        c_name = input("Enter category Name :")
        obj = M_Category(c_id,c_name)
        category.append(obj)
        x = input("do you want to add another category? (y/n) :")

def dl_ct():
    x = 'y'
    while x == 'y':
        del_c = input("Enter category Name :")
        for i in category:
            if i.c_name == del_c:
                category.remove(i)
                x = input("do you want to delete another category? (y/n) :")

def up_ct():
    x = 'y'
    while x == 'y':
        update_category = input("Enter category name you want to update: ")
        for i in category:
            if i.c_name == update_category:
                y = input("Enter new category: ")
                i.c_name = y
                x = input("do you want to update another category? (y/n) :")

def s_ct():
    x = 'y'
    while x == 'y':
        search = input("Enter category name you want to search: ")
        for i in category:
            if str(i.c_name) == str(search):
                i.print_para()
        x = input("Do you want to search again? (y/n):  ")

def display():
    for i in category:
        i.print_para()


class M_Product(M_Category):

    def __init__(self,p_id,p_name,p_cate,price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_cate = p_cate
        self.price = price

    def print_paras(self):
        print(self.p_id,self.p_name,self.p_cate,self.price)

def ad_pr():
    x = 'y'
    while x == 'y':
        p_id = int(input("Enter product ID :"))
        p_name = input("Enter product Name :")
        p_cate = input("Enter product category: ")
        price = float(input("Enter price of the product: "))
        print()
        obj1 = M_Product(p_id,p_name,p_cate,price)
        product.append(obj1)
        x = input("do you want to add another product? (y/n) :")

def dl_pr():
    x = 'y'
    while x == 'y':
        del_p = input("Enter product Name :")
        for i in product:
            if i.p_name == del_p:
                product.remove(i)
                x = input("do you want to delete another product? (y/n) :")

def u_pr():
    x = 'y'
    while x == 'y':
        update_product = input("Enter product name you want to update: ")
        for i in product:
            if i.p_name == update_product:
                y = input("Enter new product name: ")
                i.p_name = y
                x = input("do you want to update another product? (y/n) :")

def s_pr():
    x = 'y'
    while x == 'y':
        search_p = input("Enter product name you want to search: ")
        for i in product:
            if i.p_name == search_p:
                i.print_paras()
            x =input("do you want to search another product? (y/n) :")
            
def display_p():
    for i in product:
        i.print_paras()


print("WELCOME TO ONLINE SHOPPING APP...")
category = []
product = []

while True:
    choice = input("What do you want to do?:\n add = A\n delete = D\n update = U\n search = S\n display = DS\n")
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
                
                ask = input("What do you want to delete: Category = c\n, product = p\n")

                if (ask == 'c'):
                    dl_ct()
                    display()
                elif (ask == 'p'):
                    dl_pr()
                    display_p()

        case 'U':

                ask = input("What do you want to update: Category = c\n, product = p\n")

                if (ask == 'c'):
                    up_ct()
                    display()
                elif(ask == 'p'):
                    u_pr()
                    display_p()

        case 'S':

                ask = input("What do you want to search: Category = c\n, product = p\n ")

                if (ask == 'c'):
                    s_ct()
                elif(ask == 'p'):
                    s_pr()

        case 'DS':

                ask = input("What do you want to display: Category = c\n, product = p\n ")
                if (ask == 'c'):
                    display()
                elif(ask == 'p'):
                    display_p()

        case _:
            print("WRONG CHOICE")
            break
