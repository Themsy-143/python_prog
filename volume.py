f = open("D://python_prog/file_read.txt", "w")

print("Enter parameters of bottle....")
pi=22/7
ht_b = float(input("Height of cylinder: "))
rd_b= float(input("Radius of cylinder: "))

print("\nEnter parameters of ice cubes.... ")
ln_c = float(input("Enter length: "))
br_c = float(input("Enter breath: "))
ht_c= float(input("Enter height: "))

vol_c = ln_c*br_c*ht_c

qt = int(input("Enter quantity of ice cubes: "))

f_vol_c = qt * vol_c

vol_b =  (pi * rd_b * rd_b * ht_b)

space = vol_b - f_vol_c

f.write("volume of cube is = "+str(vol_c) + "cm\u00b3")

if vol_b < f_vol_c:
    print("Not enough space for juice..")
else:
    print( str(space) + " This much juice will be stored...")

f.write("\n volume of bottle is = "+str(vol_b) + "cm\u00b3")

f.write("\n empty space = "+str(space) + "cm\u00b3")

f.close()
