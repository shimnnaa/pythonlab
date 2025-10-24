n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    num=int(input("Enter elements:"))
    lst.append(num)
sum=0
for item in lst:
    sum+=item
print("Sum of all items:",sum)
