num1=int(input("enter the first integer:"))
num2=int(input("enter the second integer:"))
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
if num2!=0:
    division=num1/num2
    modulus=num1%num2
else:
    division="undefined(division by zero)"
    modulus="undefined(division by zero)"
print(f"{num1}+{num2}=multiplication}")
print(f"{num1}-{num2}={subtraction}")
print(f"{num1}*{num2}={multiplication}")
print(f"{num1}/{num2}={division}")
print(f"{num1}%{num2}={modulus}")

