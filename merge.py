n1=int(input("Enter number of items for first dictionary:"))
d1={}
for _ in range(n1):
    k=input("Enter key:")
    v=input("enter value:")
    d1[k]=v
n2=int(input("Enter number of items for second dictionary:"))
d2={}
for _ in range(n2):
     k=input("Enter key:")
     v=input("enter value:")
     d2[k]=v
merged={**d1,**d2}
print("Merged dictionary:",merged)

