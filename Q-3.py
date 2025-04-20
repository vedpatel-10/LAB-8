st = set()
n1 = input("Enter name 1: ")
n2 = input("Enter name 2: ")
n3 = input("Enter name 3: ")
n4 = input("Enter name 4: ")
n5 = input("Enter name 5: ")
st.add(n1)
st.add(n2)
st.add(n3)
st.add(n4)
st.add(n5)
print(st)

st.pop()
st.pop()
st.pop()
print(st)
st.add("hello")
print(st)

#OUTPUT:
# Enter name 1: ved 
# Enter name 2: sumit
# Enter name 3: pavan
# Enter name 4: prince
# Enter name 5: kartik
# {'ved', 'prince', 'sumit', 'pavan', 'kartik'}
# {'pavan', 'kartik'}
# {'hello', 'pavan', 'kartik'}
