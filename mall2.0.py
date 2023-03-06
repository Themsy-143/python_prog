class M_cat(object):
    def __init__(self,c_id,c_name):
        self.c_id = c_id
        self.c_name = c_name
    #set
    def set_id(self,c_id):
        self.c_id = c_id
    def set_name(self,c_name):
        self.c_name = c_name
    
    #get
    def get_id(self):
        return self.c_id 
    def get_name(self):
        return self.c_name
    def __str__(self):
        return '\nCategory id:' + str(self.get_id()) + '\nCategory name =' + str(self.get_name())

class M_pro(M_cat):
    def __init__(self,p_id,p_cat,p_name,p_price):
        self.p_id = p_id
        self.p_cat = p_cat
        self.p_name = p_name
        self.p_price = p_price
    #set
    def set_pid(self,p_id):
        self.p_id = p_id
    def set_cat(self,p_cat):
        self.p_cat = p_cat
    def set_pname(self,p_name):
        self.p_name = p_name
    def set_price(self,p_price):
        self.p_price = p_price
    
    #get
    def get_pid(self):
        return self.p_id 
    def get_cat(self):
        return self.p_cat
    def get_pname(self):
        return self.p_name
    def get_price(self):
        return self.p_price
    
    def __str__(self):
        return '\n Product id:' + str(self.get_pid())+ '\n Product category =' + str(self.get_cat()) + '\n Product name =' + str(self.get_pname())+ '\n Product price =' + str(self.get_price())

cat = []
pro = []
while True:
    choice = input('Enter Choice\n ADD : a \n UPDATE : u \n SEARCH : s \n DELETE : d \n DISPLAY : D \n:')

    match choice:  
        case 'a':
            x = input('what do you want to ADD?\n Category = c \n Product = p \n :-')
            if x == 'c':
                c_id = int(input('Enter category Id :'))
                c_name = input('Enter category Name :')
                if cat == []:
                    obj = M_cat(c_id,c_name)
                    cat.append(obj)
                else:
                    for ct in cat:
                        if ct.get_name() != c_name:
                            obj = M_cat(c_id,c_name)
                            cat.append(obj)
                            print('\n ====== Category added. ======')
                            break
                        else:
                            print('\n ====== Category already exists. ======')
            elif x == 'p':
                p_id = int(input('Enter Product Id :'))
                p_cat = input('Enter Product Category :')
                p_name = input('Enter Product Name :')
                p_price = float(input('Enter Product Price :'))
                obj1 = M_pro(p_id,p_cat,p_name,p_price)
                pro.append(obj1)
                print('\n Product added.')
            else:
                print('Wrong Choice!\n===============')

        case 'u':
            z = input("'what do you want to UPDATE?\n Category = c \n Product = p \n :-' ")
            if z == 'c':
                c_n = input('Enter category name you want to update :')
                for c in cat:
                    if c.get_name() == c_n:
                        new = input('Enter new category:')
                        c.set_name(new)
                        print('===============\n Category Updated.\n===============')
                        break
            elif z == 'p':
                p_n = input('Enter product name you want to update :')
                for p in pro:
                    if p.get_pname() == p_n:
                        while True:
                            x = input('Do you want to update Product name? (y/n):')
                            if x == 'y':
                                new = input('Enter new product name:')
                                p.set_pname(new)
                                print('===============\n Productc Name Updated.\n===============')
                                break 
                            else:
                                break 
                           
                        while True:
                            x = input('Do you want to update Product category? (y/n):')
                            if x == 'y':
                                new = input('Enter new product category:')
                                p.set_cat(new)
                                print('===============\n Productc Category Updated.\n===============')
                                break 
                            else:
                                break
                        while True:
                            x = input('Do you want to update Product price? (y/n):')
                            if x == 'y':
                                new = input('Enter new product price:')
                                p.set_price(new)
                                print('===============\n Productc Price Updated.\n===============')
                                break
                            else:
                                break
            else:
                print('Wrong Choice.\n================')

        case 's':
            x = input('Enter product name you want to Search :')
            for p in pro:
                if p.get_pname().casefold() == x.casefold():
                    print(f'==================\n name : {p.get_pname()} price : {p.get_price()}\n==================')
                    break
            else:
                print('No results found.\n==================')

        case 'd':
            x = input('Enter product name you want to Delete :')
            for p in pro:
                if p.get_pname().casefold() == x.casefold():
                    pro.remove(p)
                    print('===============\n Product deleted.\n===============')
                    break
            else:
                print('No results found.\n==================')

        case 'D':
                for c in cat:
                    print('\n============'+ c.get_name() + '=============\n')
                    for p in pro:
                        if c.get_name()==p.get_cat():
                            print(f'name : {p.get_pname()} price : {p.get_price()}')
                        else:
                            print('No results found.\n==================')
                print("\n=============================\n")

        case _:
            print('Wrong Choice.')
            break