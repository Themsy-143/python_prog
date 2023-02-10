def ad_book(list):
    book_entry = {
        "book_name" : input("Enter book name: "),
        "Author_name" : input("Enter Author name: "),
        "Book_prize" : float(input("Enter book prize: "))
        } 
    list.append(book_entry)
    return list

def del_book(list, bk_del):
    for i in list:
        if i["book_name"] == bk_del:
            print("del",i["book_name"])
            list.remove(i)
    return list

def chnge_prize(list,c_book_name,c_prize):
    for i in list:
        if i["book_name"] == c_book_name:
        
            print("change",i["Book_prize"])
            i["Book_prize"]= c_prize
    return list

n = int(input("How many books do you have?: "))
list = []
for i in range(0,n):
    book_entry = {
        "book_name" : input("Enter book name: "),
        "Author_name" : input("Enter Author name: "),
        "Book_prize" : float(input("Enter book prize: "))
        }
    list.append(book_entry)
print(list)

choice = input("What do you want to do? \nadd book = a \ndelete book = d \nchange prize = p \n---: ")

if (choice == 'a'):
    list = ad_book(list)
    print("add" , list)

elif (choice == 'd'):
    bk_del = input("Enter book name which you want to delete: ")
    list = del_book(list, bk_del)
    print("deleted" , list)

elif (choice == 'p'):
    c_book_name = input("Enter book name whose prize you want to change: ")
    c_prize = float(input("Enter new prize:  "))
    list = chnge_prize(list,c_book_name,c_prize)
    print("changed prize: ",list)

