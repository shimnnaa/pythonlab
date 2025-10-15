s=input("enter a string")
ch=s[0]
new_s=ch+s[1:].replace(ch,'$')
print("result:",new_s)
