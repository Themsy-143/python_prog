lst = [17000, 17100, 17200, 17300, 17400]
lst1 = []
for i in lst:
    x = str(i)+ '_Ce'
    lst1.append(x)
print(lst1)


eter = 0
for i in lst:
    i = str(i)+"_ce"
    lst[eter] = i
    eter+=1
print(lst)