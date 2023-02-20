office_data={}

mydata=input("how many user you want: ")
for x in range(int(mydata)):
    name=input("name: ")
    position=input("your position: ")
    dob=input("dob: ")
    temp = {}
    temp["dob"] = dob
    temp["position"]= position
    office_data[name]=temp
print(office_data)

y = input("Enter new name: ")

office_data[y] = office_data[name]
del office_data[name]

print(str(office_data))

