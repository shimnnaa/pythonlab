n=int(input("how many integer?"))
nums=[int(input("enter number:")) for _ in range (n)]
result=["over" if x>100 else x for x in nums]
print("modified list:",result)
