st = {"ashish","bhautik","ashutosh","becky","arun"}
st_a = set()
st_b = set()

for i in st:
    if (i[0] == "a" or i[0] == "A"):
        st_a.add(i)
    elif(i[0] == "b" or i[0] == "B"):
        st_b.add(i)

print(st_a)
print(st_b)

#OUTPUT:
# {'arun', 'ashish', 'ashutosh'}
# {'bhautik', 'becky'} 
