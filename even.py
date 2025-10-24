import math
result=[]
for num in range(1000,10000):
    s=str(num)
    if all(int(d)%2==0 for d in s):
        if int(math.sqrt(num))**2==num:
            result.append(num)
print("four-digit numbers with all even digits and perfect square are:")
print(result)
