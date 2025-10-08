input_string=input("enter a string:")
n=int(input("eneter the number of copies(non negative integers):"))
if n<0:
    print("error:number of copies must be inteeger")
else:
    result=input_string*n
    print(f"result:{result}")

