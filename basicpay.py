basic_pay=float(input("enetr the basic pay of the employee:"))
hra=0.10*basic_pay
ta=0.05*basic_pay
gross_salary=basic_pay+hra+ta
print(f"basic pay:{basic_pay:.2f}")
print(f"HRA (10%):{hra:.2f}")
print(f"TA (5%):{ta:.2f}")
print(f"gross salary:{gross_salary:.2f}")

