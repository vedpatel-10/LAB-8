import random
st = {random.randint(15,45) for i in range(10)}
print(st)
count = 0
count1 = 0
st1 = set()
for i in st:
    if i<30:
        count = count+1
        st1.add(i)
    elif i >35:
         count1 = count1 +1
    else:
         st1.add(i)      

print(f"Number of elements less than 30 are {count}")    
print("new set is :", st1)    

#OUTPUT:
# {33, 38, 40, 42, 43, 16, 18}
# Number of elements less than 30 are 2
# new set is : {16, 33, 18}       
