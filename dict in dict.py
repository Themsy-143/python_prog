office_data={}

ask_usr=input("how many user you want: ")
for x in range(int(ask_usr)):
    name=input("name: ")
    position=input("your position: ")
    dob=input("dob: ")
    temp = {}
    temp["dob"] = dob
    temp["position"]= position
    office_data[name]=temp
print(office_data)

while True:

    choice = int(input("What do you want to do: update name = 1/ update position = 2/ update dob = 3"))

    if (choice == 1):
        t = 'y'
        while t == 'y':
            update_name = input("Enter name you want to change: ")
            x = input("Enter new name: ")
            office_data[x]=office_data[update_name]
            del office_data[update_name]
            print(office_data)  
            t=input("do you want to update another name? (y/n) :")
                
    elif (choice == 2):
        t = 'y'
        while t == 'y':
            update_position=input("Enter position you want to change: ")
            y= input("Enter new position: ")
            office_data[update_position]['position'] = y
            print(office_data)  
            t =input("do you want to update another position? (y/n) :")
                
    elif (choice == 3):
        t = 'y'
        while t == 'y':
            update_dob=input("Enter dob you want to change: ")
            z=input("Enter new dob: ")
            office_data[update_dob]['dob']=z
            print(office_data)  
            t =input("do you want to update another dob? (y/n) :")
                
    else:
        print("WRONG CHOICE...")
