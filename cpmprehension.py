nums=list(map(int,input("enter integers:").split()))
positive=[x for x in nums if x>0]
print("positive numbers:",positive)
N=int(input("Enter N:"))
squares=[x**2 for x in range (1,N+1)]
print("Squares:",squares)
word=input("Enter a word:")
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("Vowels:",vowels)
ordinals=[ord(ch) for ch in word]
print("Ordinal values:",ordinals)
