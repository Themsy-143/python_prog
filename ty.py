# for loop
'''b is empty variable, goes in loop 5 times coz of range()function
b(0) = b(0)+"*", it prints (*) 1 time again goes in loop,
b(1) = b(1)+"*", it prints (*) 2 times and same goes on for 5 times 
and will give us pyramid shape of (*) in output'''
#a = 0
b = ""
for x in range(0,5):
    #a=a+1
    b = b + "*"
    print(b)
#print(x)

# ========================================================================================================================
'''l has a list [1,2,3,4,5,4,2,6,5,8,7,5], but here we don't want 2 in output
will apply for loop for l, after if condition to block number 2
and then continue, so this will print whole list l except number 2 '''

l=[1,2,3,4,5,4,2,6,5,8,7,5]
for y in l:
    if y ==2:
        continue
    # print(y)

# ========================================================================================================================
''' n=n+z adds every element in the list,
but the additional var should be 0 
else it'll go in infinite loop'''

m=[1,2,3,4,5,4,2,6,5,8,7,5]
n = 0
sum = 0
'''for z in m:
    n=n+z
print(n)'''

while n<=11:
    sum = m[n]+sum
    n+=1
print(sum)



   
    
