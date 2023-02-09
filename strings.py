# s = "MIDOCEAN TECHNOLOGIES"[::-1]
# print(s)

# r = s.replace("O","S")
# print(r)

st = ["suraj@gmail.com", "themsy@gmail.com", "rehmat@gmail.com", "bhavisha@gmail.com", "harsh@gmail.com"]

for i in st:
    inte = i.index("@")
    x = i[0:int(inte)]
    print(x)
    