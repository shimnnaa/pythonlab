n=int(input("Enter number of items:"))
d={}
for _ in range(n):
    key=input("enter key:")
    value=input("Enter value:")
    d[key]=value
asc={k:d[k] for k in sorted(d)}
desc={k:d[k] for k in sorted (d ,reverse=True)}
print("Ascenting:",asc)
print("Descenting:",desc)
