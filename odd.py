numbers=list(map(int,input("enetr integers seperated by space:").split()))
odd_numbers=[num for num in numbers if num%2!=0]
print("list after removing even numbers:",odd_numbers)
