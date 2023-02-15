# for loop
'''n stores 11 number, 
loop will go round 11 times coz of range() function
prints 11 numbers'''

n = 11
for x in range (1, n):
    print(x)

# ========================================================================================================================

'''a stores 10 number,
b is empty variable, it'll store data after going in loop
loop will go round 10 times coz of range() function
first b is 0 equal 0+a(range starts from 1)
print b = 1, again does same for 10 times'''

a = 10
b=""
for k in range(1, a):
    b = b + str(k)
print(b)

# ========================================================================================================================

'''c equals to 10, d equals 1
goes in loop for 10 times, d(0) = i(0) + d(1), prints d
again d(1) = i(1) + d(2), prints d, this same happens 10 times'''
c = 10
d = 1
for i in range(0,c):
    d=i+d
print(d)





